# -*- coding: utf-8 -*-
import csv
import time
import traceback as tr
import bluetooth as bt
from ..library import connect
from ..config import address as ad

addr = ad.server_address
PORT = 3


class Connection:
    def __init__(self):
        self.recv_data = []
        self.send_data = []
        self.ras = connect.Connection("sev", addr, PORT)
        while True:
            if self.ras.connectBluetooth(self.ras.bdAddr, self.ras.port):
                break

    def send(self, value):
        self.data = value
        self.sendtime = time.time()
        self.ras.sock.send((self.data).to_bytes(1, "little"))
        self.res_data.append([time.time(), self.data])
        print("target={0} send:{1}".format(self.id, self.data))

    def receive(self):
        self.ras.accept()
        self.rcv_data = int.from_bytes(self.ras.sock.recv(1024), "little")
        self.recv_data.append([time.time(), self.rcv_data])
        print("host:{0} recv:{1}".format("server", self.rcv_data))

    def write_logs(self):
        self.path = "../log/cdata{0}.csv".format(PORT-1)
        self.file = open(self.path, "w")
        self.w = csv.writer(self.file)
        self.w.writerows(self.recv_data)
        self.file.close()

    def __del__(self):
        self.write_logs()
        self.ras.disConnect()


def main():
    ras = Connection()
    while True:
        try:
            ras.receive()
        except bt.BluetoothError:
            break
    del ras


if __name__ == '__main__':
    main()
