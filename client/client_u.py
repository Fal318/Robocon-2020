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


PATH = "365.csv"
MODE = 0
# メロディー:0, コード:1


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


def generate_send_data(path: str, bpm) -> list:
    df = pd.read_csv(path)
    original_data = pd.DataFrame(index=None)
    for key in head.UKULELE:
        original_data[key] = df[key].fillna(0)
    if MODE:
        for key in ["FRET1", "FRET2", "FRET3", "FRET4"]:
            original_data[key] = [0 for _ in range(len(original_data[key]))]
    else:
        original_data["STROKE"] = [
            0 for _ in range(len(original_data["STROKE"]))]

    return [calculate_send_data(bpm, *list(row[1:]))
            for row in original_data.itertuples()]


def calculate_send_data(bpm, *args) -> int:

    timing, bownum, fret1, fret2, fret3, fret4, stroke, chord, face, neck = args
    send_val = ((bpm-60)//5)*2**28 + timing * 2**27 + bownum * 2**24 + \
        fret1 * 2**21 + fret2 * 2**18+fret3 * 2**15 + \
        fret4*2**12 + stroke*2**11 + chord * 2**5 + face*2**2+neck
    return int(send_val)


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
    generated_data = generate_send_data(f"../data/fixed/{PATH}", bpm)
    lag = Lag(60/bpm)
    try:
        if start_time-time.time() > 0.2:
            time.sleep(start_time-time.time()-0.2)
        while start_time - time.time() > 0:
            time.sleep(0.001)

        if not maicon.is_aivable:
            return

        for sd in generated_data:
            send_time = time.time()
            time.sleep(config.UKULELE_DELAY)
            maicon.write(sd)
            print(sd)
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
    print(max(generate_send_data(f"../data/fixed/{PATH}", 105)))
    exit(0)
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
