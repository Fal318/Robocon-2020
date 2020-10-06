# -*- coding: utf-8 -*-
"""パーカッション"""
import time
import serial
import pandas as pd
import bluetooth as bt
from library import head, serial_connect

LAG = 0.01

def generate_send_data(path: str) -> list:
    """送信するデータの配列とBPMを返す"""
    original_df = pd.read_csv(path, index=False)
    original_data = pd.DataFrame()
    for key in head.UKULELE:
        original_data[key] = original_df[key].fillna(0)
    return [[calculate_send_data(*list(d)) for d in original_data.itertuples()], original_data["bpm"]]


def calculate_send_data(string: int, bpm: int, timing: bool,
                        stroke: bool, chord: int, face: int, neck: int) -> list:
    """各データから送信する値を計算して1Byteごとのlistにして返す"""
    send_val = string*2**20 + bpm*2**13 + timing * 2**12 + \
        stroke * 2**11 * chord * 2**5 + face*2**2+neck
    return [send_val & 16711680, send_val & 65280, send_val & 255]


def get_period(bpm) -> float:
    """BPMから周期を返す"""
    return 60 / bpm


def main():
    """main"""
    # generated_data = generate_send_data("../data/data.csv")
    generated_data = []
    server_socket = bt.BluetoothSocket(bt.RFCOMM)
    maicon = None
    try:
        server_socket.bind(("", 1))
        server_socket.listen(1)
        client_socket = server_socket.accept()[0]
        maicon = serial_connect.Serial_Connection("/dev/mbed", 115200)
        print("Connect")
        client_socket.send((1).to_bytes(1, "little"))
        start_time = int.from_bytes(client_socket.recv(64), "little")/10000000
        if start_time < 0:
            raise Exception("Failed")
        if start_time-time.time() > 0.2:
            time.sleep(start_time-time.time()-0.2)
        while start_time - time.time() > 0:
            time.sleep(0.001)

        for send_data, bpm in zip(*generated_data):
            send_time = time.time()
            time.sleep(LAG)
            for s in send_data:
                maicon.write(s)
            time.sleep(time.time()-send_time-get_period(bpm))
    except KeyboardInterrupt:
        print("Connection Killed")
    except serial.SerialException:
        server_socket.send((1).to_bytes(1, "little"))
        start_time = int.from_bytes(client_socket.recv(64), "little")/10000000
        print(start_time)
    else:
        print("Connection Ended")
    finally:
        del maicon


if __name__ == "__main__":
    main()
