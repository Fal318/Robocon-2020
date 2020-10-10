# -*- coding: utf-8 -*-
"""パーカッション"""
import sys
import time
import threading
import serial
import pandas as pd
import bluetooth as bt
from cobs import cobs
from library import head, serial_connect

DELAY = 0


class Lag:
    def __init__(self):
        self.__start_time = None
        self.__period = []

    def get_lag(self, period, send_time):
        if self.__start_time is None:
            self.__start_time = send_time
        self.__period.append(period)
        return self.__start_time + sum(self.__period) - time.time()


def generate_cobs(value: int, byte_size: int = 3) -> bytes:
    encoded = cobs.encode(value.to_bytes(byte_size, "big"))+b'\x00'
    return [encoded[i:i+1] for i in range(byte_size+2)]


def calculate_send_data(args: list) -> list:
    """送信データを1Byteごとに分割"""
    bowstring, bpm, timing, stroke, chord, face, neck = args
    send_val = bowstring*2**20 + bpm*2**13 + timing * 2**12 + \
        stroke * 2**11 * chord * 2**5 + face*2**2+neck
    return generate_cobs(send_val)


def generate_send_data(path: str) -> list:
    """送信するデータの配列とBPMを返す"""
    original_df = pd.read_csv(path)
    original_data = pd.DataFrame()
    for key in head.UKULELE:
        original_data[key] = original_df[key].fillna(0)
    return [[calculate_send_data(*list(d))
             for d in original_data.itertuples()], original_data["bpm"]]


def get_period(bpm) -> float:
    """BPMから周期を返す"""
    return 60 / bpm


def setup() -> list:
    """セットアップ"""
    try:
        server_socket = bt.BluetoothSocket(bt.RFCOMM)
        server_socket.bind(("", 1))
        server_socket.listen(1)
        client_socket = server_socket.accept()[0]
        maicon = serial_connect.Serial_Connection("/dev/mbed", 115200)
        client_socket.send(b'\x01')
        start_time = int.from_bytes(client_socket.recv(64), "little")/10000000
    except serial.SerialException:
        sys.exit("Setup Failed")
    except bt.BluetoothError:
        sys.exit("Setup Failed")
    else:
        return [client_socket, maicon, start_time]


def status_check(socket: bt.BluetoothSocket) -> int:
    """ステータスのチェック"""
    while True:
        try:
            recv = int.from_bytes(socket.recv(1), "little")
        except bt.BluetoothError:
            continue
        else:
            return recv


def main_connection(socket, maicon, start_time):
    """main"""
    # generated_data = generate_send_data("../data/data.csv")
    generated_data = [[[[1, 1, 1] for _ in range(
        100)], [120 for _ in range(100)]] for _ in range(100)]  # test data
    lag = Lag()
    try:

        if start_time <= 0:
            raise Exception("Failed")
        if start_time-time.time() > 0.2:
            time.sleep(start_time-time.time()-0.2)
        while start_time - time.time() > 0:
            time.sleep(0.001)
        print(time.time())
        if not maicon.is_aivable:
            return
        for send_data, bpms in generated_data:
            for sd, bpm in zip(send_data, bpms):
                send_time = time.time()
                time.sleep(DELAY)
                for s in sd:
                    maicon.write(s)
                time.sleep(lag.get_lag(get_period(bpm), send_time))

    except:
        print("Process is Failed")
    else:
        print("Connection Ended")
    finally:
        socket.send(b'\x01')
        del maicon


def main():
    socket, maicon, start_time = setup()
    sub_thread = threading.Thread(
        target=main_connection, args=([socket, maicon, start_time]))
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
