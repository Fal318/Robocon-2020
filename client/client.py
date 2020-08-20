# -*- coding: utf-8 -*-
"""クライアント側の代用"""
import csv
import time
import bluetooth as bt


PORT = 1

server_socket = bt.BluetoothSocket(bt.RFCOMM)
recv_data = []
try:
    server_socket.bind(("", PORT))
    server_socket.listen(1)
    client_socket, address = server_socket.accept()
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

file = open("../data/log/cdata{0}.csv".format(PORT-1), "w")

w = csv.writer(file)
w.writerows(recv_data)
file.close()
