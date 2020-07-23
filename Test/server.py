import csv
import sys
import time
import random
import signal
import struct
import traceback
import bluetooth as bt
import RN42
import address as ad

period = 0.1
addr = ad.client_address

res_data = []


def connect():
    global ras
    try:
        ras = RN42.RN42("ras", ad.client_address, 1)
        ras.connectBluetooth(ras.bdAddr, ras.port)
    except:
        sys.exit("Connection Failed")
    else:
        print("Connect")


def send(signum, frame):
    data = random.randint(0, 255)
    ras.sock.send((data).to_bytes(1, "little"))
    res_data.append([time.time(), data])
    print("send:{0}".format(data))


def write_logs():
    file = open("./sdata.csv", "w")
    w = csv.writer(file)
    w.writerows(res_data)
    file.close()


def main():
    connect()

    signal.signal(signal.SIGALRM, send)
    signal.setitimer(signal.ITIMER_REAL, period, period)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Connection Killed")
    except signal.ItimerError:
        print("Signal Error")
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    write_logs()


if __name__ == "__main__":
    main()
