# -*- coding: utf-8 -*-
import csv
import time
import random
import threading
import bluetooth as bt
from ..library import connect
from ..config import address as ad

PERIOD = 0.2
LOOP = 500


class Connection:
    def __init__(self, i: int):
        self.res_data = []
        self.id = i
        try:
            self.addr = ad.client_address[i]
        except IndexError:
            self.aivable = False
            return

        self.ras = connect.Connect("ras{0}".format(
            self.id), self.addr, self.id+1)
        if self.ras.connectBluetooth(self.ras.bdAddr, self.ras.port):
            self.aivable = True
            print("Connect")
        else:
            self.aivable = False
            print("Connection Failed")

    def is_aivable(self):
        return self.aivable

    def send(self):
        self.data = random.randint(0, 255)
        self.sendtime = time.time()
        self.ras.sock.send((self.data).to_bytes(1, "little"))
        self.res_data.append([time.time(), self.data])
        print("target={0} send:{1}".format(self.id, self.data))

    def send_arr(self):
        pass

    def receive(self):
        self.rcv_data = int.from_bytes(self.ras.sock.recv(1024), "little")
        print("host:{0} recv:{1}".format(self.id, self.rcv_data))

    def write_logs(self):
        self.path = "../log/sdata{0}.csv".format(self.id)
        self.file = open(self.path, "w")
        self.w = csv.writer(self.file)
        self.w.writerows(self.res_data)
        self.file.close()

    def main_process(self):
        for _ in range(LOOP):
            try:
                self.send()
                self.itv = PERIOD - (time.time() - self.sendtime)
                time.sleep(self.itv)
            except KeyboardInterrupt:
                print("Connection Killed")
                break
            except bt.BluetoothError:
                print("Connection Killed")
                break

    def __del__(self):
        self.write_logs()
        self.ras.disConnect()


def main():
    rass, threads = [], []
    for i in range(2):
        ras = Connection(i)
        if not(ras.is_aivable()):
            continue
        rass.append(ras)
        thread = threading.Thread(target=ras.main_process)
        threads.append(thread)
    for t in threads:
        t.start()

    for ras in rass:
        del ras


if __name__ == "__main__":
    main()
