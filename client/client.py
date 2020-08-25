# -*- coding: utf-8 -*-
"""クライアント側の代用プログラム"""
import bluetooth as bt


def main():
    """main"""
    PORT = 1
    server_socket = bt.BluetoothSocket(bt.RFCOMM)

    try:
        server_socket.bind(("", PORT))
        server_socket.listen(1)
        client_socket, address = server_socket.accept()
        print("Connect")
        rcv = None
        while rcv != 0:
            rcv = int.from_bytes(client_socket.recv(1024), "little")
            print(f"recv:{rcv}")
    except KeyboardInterrupt:
        print("Connection Killed")
    else:
        print("Connection Ended")


if __name__ == "__main__":
    main()
