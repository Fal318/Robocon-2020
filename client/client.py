# -*- coding: utf-8 -*-
"""クライアント側の代用プログラム"""
import time
import csv
import bluetooth as bt


def main():
    """main"""

    server_socket = bt.BluetoothSocket(bt.RFCOMM)
    recv_data = []
    try:
        server_socket.bind(("", 1))
        server_socket.listen(1)
        client_socket = server_socket.accept()[0]
        print("Connect")
        while True:
            rcv = int.from_bytes(client_socket.recv(64), "little")
            recv_data.append([time.time(), rcv])
            print(f"recv:{rcv}")
            if rcv == 0:
                break
    except KeyboardInterrupt:
        print("Connection Killed")
    else:
        print("Connection Ended")

    file = open("../data/log/cdata.csv", "w")

    w = csv.writer(file)
    w.writerows(recv_data)
    file.close()


if __name__ == "__main__":
    main()
