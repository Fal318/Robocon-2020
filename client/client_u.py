# -*- coding: utf-8 -*-
"""クライアント側"""
import csv
import time
import bluetooth as bt
from library import serial_connect


class Log:
    """ログの管理"""

    def __init__(self):
        self.__log: list = []

    def add(self, data: float):
        """データの追加"""
        self.__log.append(data)

    def __del__(self):
        csv.writer(open("../data/csv/cdata.csv", "w")).writerows(self.__log)


def main():
    """main"""
    server_socket = bt.BluetoothSocket(bt.RFCOMM)
    maicon = None
    log = Log()
    try:
        server_socket.bind(("", 1))
        server_socket.listen(1)
        client_socket = server_socket.accept()[0]
        maicon = serial_connect.Serial_Connection("/dev/mbed", 9600)
        print("Connect")
        while True:
            rcv = int.from_bytes(client_socket.recv(64), "little")
            rcv_time = time.time()
            maicon.write(rcv)
            server_socket.send(int(rcv_time*10000000))
            log.add(rcv_time)
            if rcv == -1:
                break
    except KeyboardInterrupt:
        print("Connection Killed")
    else:
        print("Connection Ended")
    finally:
        del log, maicon


if __name__ == "__main__":
    main()
