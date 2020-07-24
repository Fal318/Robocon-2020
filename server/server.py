# -*- coding: utf-8 -*-
import csv
import sys
import time
import random
import signal
import struct
import traceback
import threading
import bluetooth as bt
import RN42
import address

PERIOD = 0.05
LOOP = 500


class Connection:
    def __init__(self, i: int):
        self.res_data = []
        self.id = i
        try:
            self.addr = address.client_address[i]
        except IndexError:
            self.aivable = False
            return
        try:
            self.ras = RN42.RN42("ras{0}".format(self.id), self.addr, 1)
            self.ras.connectBluetooth(self.ras.bdAddr, self.ras.port)
        except:
            self.aivable = False
            print("Connection Failed")
        else:
            self.aivable = True
            print("Connect")

    def sighandler(self, signr, handler):
        pass

    def is_aivable(self):
        return self.aivable

    def send(self):
        self.data = random.randint(0, 255)
        self.sendtime = time.time()
        self.ras.sock.send((self.data).to_bytes(1, "little"))
        self.res_data.append([time.time(), self.data])
        print("target={0} send:{1}".format(self.id, self.data))

    def write_logs(self):
        self.path = "../log/sdata_{0}.csv".format(self.id)
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
            except:
                traceback.print_exc()
                print(self.itv)
                print("Connection Killed")
                break

    def __del__(self):
        self.write_logs()
        self.ras.disConnect()


def main():
    rass, threads = [], []
    for i in range(2):
        try:
            ras = Connection(i)
            if not(ras.is_aivable()):
                continue
            rass.append(ras)
            thread = threading.Thread(target=ras.main_process)
            threads.append(thread)
        except:
            traceback.print_exc()
            continue
    for t in threads:
        t.start()
        t.join()
    for ras in rass:
        del ras


if __name__ == "__main__":
    main()
