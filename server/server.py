"""ホスト側のプログラム"""
# -*- coding: utf-8 -*-
import csv
import time
import random
import threading
import bluetooth as bt
import address as ad
from library import connect
PERIOD: float = 0.2
LOOP: int = 500

"""
PERIOD:実行周期(sec)
LOOP:実行回数(回)
"""


class Connection:
    """
    通信関連のクラス
    """

    def __init__(self, i: int):

        self.file = None
        self.sendtime = None
        self.rcv_data = None
        self.send_data: list = []
        self.proc_id: int = i

        try:
            self.ras = connect.Connect("ras{0}".format(
                self.proc_id), ad.CLIENT[i], self.proc_id+1)
            if self.ras.connectBluetooth(self.ras.bdAddr, self.ras.port):
                self.aivable = True
                print("Connect")
            else:
                self.aivable = False
                print("Connection Failed")
        except IndexError:
            self.aivable = False

    def is_aivable(self) -> bool:
        """
        プロセスが有効かどうかを返す関数
        """
        return self.aivable

    def send(self, data):
        """
        データ(整数値)を送信する関数
        """
        self.sendtime = time.time()
        self.ras.sock.send((data).to_bytes(1, "little"))
        self.send_data.append([time.time(), data])
        print("target={0} send:{1}".format(self.proc_id, data))

    def send_arr(self):
        """
        データ(配列)を送信する関数
        """
        return self

    def receive(self):
        """
        データを受信する関数
        """
        self.rcv_data = int.from_bytes(self.ras.sock.recv(1024), "little")
        print("host:{0} recv:{1}".format(self.proc_id, self.rcv_data))

    def write_logs(self):
        """
        送受信のログをcsvに書き込む関数
        """
        self.file = open(f"../log/sdata{self.proc_id}.csv", "w")
        csv.writer(self.file).writerows(self.send_data)
        self.file.close()

    def main_process(self):
        """
        メインプロセス
        """
        for _ in range(LOOP):
            try:
                self.send(random.randint(0, 255))
                time.sleep(PERIOD - (time.time() - self.sendtime))
            except KeyboardInterrupt:
                print("Connection Killed")
                break
            except bt.BluetoothError:
                print("Connection Killed")
                break

    def __del__(self):
        self.ras.disConnect()
        if self.aivable:
            return
        self.write_logs()


def main():
    """
    main
    """
    rass, threads = [], []
    for i in range(2):
        ras = Connection(i)
        if ras.is_aivable():
            rass.append(ras)
            thread = threading.Thread(target=ras.main_process)
            threads.append(thread)

    for thread in threads:
        thread.start()

    for ras in rass:
        del ras


if __name__ == "__main__":
    main()
