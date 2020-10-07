# -*- coding: utf-8 -*-
"""ウクレレ"""
import time
import threading
import pandas as pd
import bluetooth as bt
from library import head, serial_connect

BPM = 120
LAG = 0
PERIOD = 60/BPM


def generate_send_data(path: str) -> list:
    original_df = pd.read_csv(path, index=False)
    original_data = pd.DataFrame()
    for key in head.UKULELE:
        original_data[key] = original_df[key].fillna(0)
    return [calculate_send_data(*list(d)) for d in original_data.itertuples()]


def calculate_send_data(string: int, bpm: int, timing: bool,
                        stroke: bool, chord: int, face: int, neck: int) -> list:
    send_val = string*2**20 + bpm*2**13 + timing * 2**12 + \
        stroke * 2**11 * chord * 2**5 + face*2**2+neck
    return [send_val & 16711680, send_val & 65280, send_val & 255]


def setup() -> list:
    try:
        server_socket = bt.BluetoothSocket(bt.RFCOMM)
        server_socket.bind(("", 1))
        server_socket.listen(1)
        client_socket = server_socket.accept()[0]
        maicon = serial_connect.Serial_Connection("/dev/mbed", 115200)
        client_socket.send(b'\x01')
        start_time = int.from_bytes(client_socket.recv(64), "little")/10000000
        if start_time <= 0:
            raise Exception("Failed")
    except:
        raise Exception("Setup Failed")
    else:
        return [server_socket, maicon, start_time]


def status_check(socket: bt.BluetoothSocket) -> int:
    while True:
        try:
            recv = int.from_bytes(socket.recv(1), "little")
        except bt.BluetoothError:
            continue
        else:
            return recv


def main_connection(maicon, start_time):
    """main"""
    #send_data = generate_send_data("../data/data.csv")
    send_data = []
    try:
        if start_time-time.time() > 0.2:
            time.sleep(start_time-time.time()-0.2)
        while start_time - time.time() > 0:
            time.sleep(0.001)
        print(time.time())
        if not maicon.is_aivable:
            return
        for sd in send_data:
            send_time = time.time()
            time.sleep(LAG)
            for s in sd:
                maicon.write(s)
            time.sleep(PERIOD+send_time-time.time())
    except KeyboardInterrupt:
        print("Connection Killed")
    else:
        print("Connection Ended")


def main():
    soket, maicon, start_time = setup()
    sub_thread = threading.Thread(
        target=main_connection, args=(maicon, start_time))
    main_thread = threading.Thread(
        target=status_check, args=(soket, start_time))
    sub_thread.setDaemon(True)
    main_thread.start()
    sub_thread.start()
    sub_thread.join()
    exit(0)


if __name__ == "__main__":
    main()
