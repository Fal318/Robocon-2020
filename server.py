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

PERIOD = 0.1
LOOP = 10000


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

    def is_aivable(self):
        return self.aivable

    def send(self, signam, frame):
        self.data = random.randint(0, 255)
        self.ras.sock.send((self.data).to_bytes(1, "little"))
        self.res_data.append([time.time(), self.data])
        print("target={0} send:{1}".format(self.id, self.data))

    def write_logs(self):
        self.path = "./log/sdata_{0}.csv".format(self.id)
        self.file = open(self.path, "w")
        self.w = csv.writer(self.file)
        self.w.writerows(self.res_data)
        self.file.close()

    def main_process(self):
        try:
            signal.signal(signal.SIGALRM, self.send)
            signal.setitimer(signal.ITIMER_REAL, PERIOD, PERIOD)
            for _ in range(LOOP):
                time.sleep(1)
        except KeyboardInterrupt:
            print("Connection Killed")
            return
        except:
            traceback.print_exc()
            print("Connection Killed")
            return

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
            continue
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    for ras in rass:
        del ras


if __name__ == "__main__":
    main()
