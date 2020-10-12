# -*- coding: utf-8 -*-
"""ウクレレ"""
import sys
import time
import threading
import serial
import bluetooth
import pandas as pd
import config
from library import head, serial_connect


class Lag:
    def __init__(self, period):
        self.__start_time = None
        self.__period = period
        self.__loop_count = 0

    def get_lag(self, send_time):
        self.__loop_count += 1
        if self.__start_time is None:
            self.__start_time = send_time
        return self.__start_time + self.__period*self.__loop_count - time.time()


def generate_send_data(path: str) -> list:
    original_df = pd.read_csv(path, header=False)
    original_data = pd.DataFrame()
    for key in head.UKULELE:
        original_data[key] = original_df[key].fillna(0)
    return [[calculate_send_data(*list(d))
             for d in original_data.itertuples()], original_data["bpm"]]


def calculate_send_data(bpm: int, timing: bool, bownum: int,
                        fret1: int, fret2: int, fret3: int, fret4: int,
                        stroke: bool, chord: int, face: int, neck: int) -> int:
    send_val = bpm*2**28 + timing * 2**27 + bownum * 2**24 + \
        fret1 * 2**21 * fret2 * 2**18*fret3 * 2**15 * \
        fret4*12 * stroke*2**11 * chord * 2**5 + face*2**2+neck
    return send_val


def setup() -> list:
    try:
        server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_socket.bind(("", 1))
        server_socket.listen(1)
        client_socket = server_socket.accept()[0]
        bpm = int.from_bytes(client_socket.recv(8), "big")
        maicon = serial_connect.Connection(
            dev="/dev/ttyACM0", rate=115200, data_size=config.BYTE_SIZE)
        client_socket.send(b'\x01')
        start_time = int.from_bytes(client_socket.recv(64), "big")/10000000
        if start_time <= 0:
            raise Exception("Failed")
    except serial.SerialException:
        sys.exit("Setup Failed")
    except bluetooth.BluetoothError:
        sys.exit("Setup Failed")
    else:
        return [client_socket, maicon, start_time, bpm]


def status_check(socket: bluetooth.BluetoothSocket) -> int:
    while True:
        try:
            recv = int.from_bytes(socket.recv(1), "big")
        except bluetooth.BluetoothError:
            continue
        else:
            return recv


def main_connection(socket, maicon, start_time, bpm):
    """main"""
    #generated_data = generate_send_data("../data/data.csv")
    generated_data = [[i for i in range(1, 10000)], [
        480 for _ in range(100)]]  # test data
    lag = Lag(60/bpm)
    try:
        if start_time-time.time() > 0.2:
            time.sleep(start_time-time.time()-0.2)
        while start_time - time.time() > 0:
            time.sleep(0.001)

        if not maicon.is_aivable:
            return

        for sd, bpm in zip(*generated_data):
            send_time = time.time()
            time.sleep(config.UKULELE_DELAY)
            maicon.write(sd)
            time.sleep(lag.get_lag(send_time))
    except KeyboardInterrupt:
        print("Connection End")
    except bluetooth.BluetoothError:
        print("Connection Killed")
    else:
        print("Connection Ended")
    finally:
        del maicon
        socket.send(b'\x01')


def main():
    socket, maicon, start_time, bpm = setup()

    print(bpm)

    sub_thread = threading.Thread(
        target=main_connection, args=([socket, maicon, start_time, bpm]))
    main_thread = threading.Thread(
        target=status_check, args=([socket]))
    sub_thread.setDaemon(True)
    main_thread.start()
    sub_thread.start()
    main_thread.join()
    if sub_thread.is_alive():
        print("Process is Killed from master")
    sys.exit(0)


if __name__ == "__main__":
    main()
