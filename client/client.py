# -*- coding: utf-8 -*-
"""クライアント側の代用プログラム"""
import csv
import time
import bluetooth as bt
import serial_connect


def main():
    """main"""
    server_socket = bt.BluetoothSocket(bt.RFCOMM)
    maicon = None
    try:
        server_socket.bind(("", 1))
        server_socket.listen(1)
        client_socket = server_socket.accept()[0]
        maicon = serial_connect.Serial_Connection("/dev/mbed", 9600)
        print("Connect")
        while True:
            rcv = int.from_bytes(client_socket.recv(64), "little")
            maicon.write(rcv)
            print(f"recv:{rcv}")
            if rcv == 0:
                break
    except KeyboardInterrupt:
        print("Connection Killed")
    else:
        print("Connection Ended")
    finally:
        del maicon


if __name__ == "__main__":
    main()
