# -*- coding: utf-8 -*-
"""ウクレレ"""
import sys
import time
import threading
import serial
import bluetooth
import pandas as pd
import config
from library import bt, head, serial_connect


PATH = "hand.csv"
MODE = 0
# メロディー:0,コード:1


class Lag:
    def __init__(self, period):
        self.__start_time = None
        self.__period = 0.01
        self.__loop_count = 0

    def get_lag(self, send_time):
        self.__loop_count += 1
        if self.__start_time is None:
            self.__start_time = send_time
        if self.__start_time + self.__period*self.__loop_count - time.time() < 0:
            return 0
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
        for key in ["CHORD", "STROKE"]:
            original_data[key] = [0 for _ in range(len(original_data[key]))]

    return [calculate_send_data(bpm, *list(row[1:]))
            for row in original_data.itertuples()]


def calculate_send_data(bpm, *args) -> int:

    timing, bownum, fret1, fret2, fret3, fret4, stroke, chord, face, neck = args
    send_val = 9*2**28 + timing * 2**27 + bownum * 2**24 + \
        fret1 * 2**21 + fret2 * 2**18+fret3 * 2**15 + \
        fret4*2**12 + stroke*2**11 + chord * 2**5 + face*2**2+neck
    return int(send_val)


def setup() -> list:
    try:
        bt_sock = bt.BluetoothChild(1)
        bt_sock.connect()
        bpm = bt_sock.receive(8)
        maicon = serial_connect.Connection(
            dev="/dev/ttyUSB0", rate=115200, data_size=config.BYTE_SIZE)
        bt_sock.send(1, 1)
        start_time = bt_sock.receive(64)/10000000
        if start_time <= 0:
            raise Exception("Failed")
    except serial.SerialException:
        sys.exit("Setup Failed")
    except bluetooth.BluetoothError:
        sys.exit("Setup Failed")
    else:
        return [bt_sock, maicon, start_time, bpm]


def format_data(value):
    timing, bownum = int(
        (value & 2**27) / 2**27), int((value & 0b111100000000000000000000000) / 2**24)
    f1, f2 = int((value & 2**21) / 2**21), int((value & 2**18) / 2**18)
    f3, f4 = int((value & 2**15) / 2**15), int((value & 2**12) / 2**12)
    stroke, chord = int((value & 2**11) / 2**11), int((value & 2**5) / 2**5)
    face, neck = int((value & 2**2) / 2**2), int(value & 2**0)
    bpm = int((value & 0b11110000000000000000000000000000)/2**28)*5+60
    return f"bpm:{bpm}, t:{timing}, b:{bownum}, f1:{f1}, f2:{f2}, f3:{f3}, f4:{f4}, s:{stroke}, c:{chord}, f:{face}, n:{neck}"


def status_check(socket: bluetooth.BluetoothSocket) -> int:
    while True:
        try:
            receive = socket.receive(1)
        except bluetooth.BluetoothError:
            print("BluetoothError")
            socket.send(1, 1)
            return
        else:
            return receive


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
        play_start = time.time()
        for sd in generated_data:
            send_time = time.time()
            time.sleep(config.UKULELE_DELAY)
            maicon.write(sd)
            print(f"{'{:.5f}'.format(time.time() - play_start)} {format_data(sd)}")
            time.sleep(lag.get_lag(send_time))
    except KeyboardInterrupt:
        print("Connection End")
    except bluetooth.BluetoothError:
        print("Connection Killed")
    else:
        print("Connection Ended")
    finally:
        del maicon
        socket.send(1, 1)


def main():
    socket, maicon, start_time, bpm = setup()

    sub_thread = threading.Thread(
        target=main_connection, args=([socket, maicon, start_time, bpm]))
    main_thread = threading.Thread(
        target=status_check, args=([socket]))
    sub_thread.setDaemon(True)
    main_thread.start()
    sub_thread.start()
    try:
        main_thread.join()
        if sub_thread.is_alive():
            print("Process is Killed from master")
    except KeyboardInterrupt:
        socket.send(1, 1)


if __name__ == "__main__":
    main()
