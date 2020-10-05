# -*- coding: utf-8 -*-
"""クライアント側"""
import time
import pandas as pd
import bluetooth as bt
from library import head, serial_connect

BPM = 120
LAG = 0.01


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


def main():
    """main"""
    period = 60/BPM
    send_data = generate_send_data("../data/data.csv")
    server_socket = bt.BluetoothSocket(bt.RFCOMM)
    maicon = None
    try:
        server_socket.bind(("", 1))
        server_socket.listen(1)
        client_socket = server_socket.accept()[0]
        maicon = serial_connect.Serial_Connection("/dev/mbed", 9600)
        print("Connect")
        client_socket.send(1)
        start_time = int.from_bytes(client_socket.recv(64), "little")/10000000
        if start_time-time.time() > 0.2:
            time.sleep(start_time-time.time()-0.2)
        while start_time - time.time() > 0:
            time.sleep(0.001)

        for sd in send_data:
            send_time = time.time()
            time.sleep(LAG)
            for s in sd:
                maicon.write(s)
            time.sleep(time.time()-send_time-period)
    except KeyboardInterrupt:
        print("Connection Killed")
    else:
        print("Connection Ended")
    finally:
        del maicon


if __name__ == "__main__":
    main()
