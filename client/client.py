"""クライアント側"""
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
    data = 1
    while data != 0:
        data = int.from_bytes(client_socket.recv(64), "little")
        recv_data.append([time.time(), data])
        print(f"recv:{data}")
except KeyboardInterrupt:
    print("Connection Killed")
else:
    print("Connection Ended")

file = open("../log/cdata{0}.csv".format(PORT-1), "w")

w = csv.writer(file)
w.writerows(recv_data)
file.close()
