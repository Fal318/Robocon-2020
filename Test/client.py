import csv
import time
import traceback as tr
import struct
import bluetooth as bt
import address as ad

addr = ad.server_address
PORT = 1

server_socket = bt.BluetoothSocket(bt.RFCOMM)
recv_data = []
try:
    server_socket.bind(("", PORT))
    server_socket.listen(1)
    client_socket, address = server_socket.accept()
    while True:
        data = client_socket.recv(1024)
        recv_data.append([time.time(), data])
except:
    tr.print_exc()

file = open("./cdata.csv", "w")

w = csv.writer(file)
w.writerows(recv_data)
file.close()
