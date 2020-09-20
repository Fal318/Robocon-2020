# -*- coding: utf-8 -*-
"""送信側のプログラム"""
import sys
import time
import threading
import bluetooth as bt
import address as ad
from library import bt_connect
from library.csv_to_list import csv_to_senddata


args = sys.argv
is_debug = False
if len(args) > 1 and args[1] == "-d":
    is_debug = True


TARGET: int = 2
PERIOD: float = 0.1

"""
TARGET:接続する台数
PERIOD:実行周期(sec)
id:
    0:ウクレレ
    1:パーカッション
"""

class Connection:
    """通信を定周期で行う"""

    def __init__(self, proc_id: int):
        self.sending_data: list = csv_to_senddata(proc_id)  # 送るデータ
        self.rcv_data: list = []  # 受け取ったデータ
        self.sendtime: float = None  # 最後に送信をした時間
        self.proc_id: int = proc_id  # プロセスを識別するID

        try:
            # 通信用のインスタンスを生成
            self.ras = bt_connect.Connect("ras{0}".format(
                self.proc_id), ad.CLIENT[proc_id], 1, is_debug)

            if self.ras.connectbluetooth(self.ras.bdaddr, self.ras.port):
                self.aivable = True
                print("Connect")
            else:
                self.aivable = False
                print("Connection Failed")
        except IndexError:
            self.aivable = False

    def is_aivable(self) -> bool:
        """プロセスが有効かどうかを返す"""
        return self.aivable

    def sender(self, data: int):
        """データ(整数値)を送信する"""
        self.sendtime = time.time()
        self.ras.sock.send((data).to_bytes(1, "little"))
        print("target={0} send:{1}".format(self.proc_id, data))

    def main_process(self, period: int):
        """メインプロセス"""
        try:
            for send in self.sending_data[0]:
                self.sender(send)
                time.sleep(period - (time.time() - self.sendtime))
        except KeyboardInterrupt:
            self.sender(0)
            print("Connection Killed")
        except ValueError:
            self.sender(0)
            print("周期が早すぎます")
        except bt.BluetoothError:
            print("Connection Killed")
        else:
            self.sender(0)

    def __del__(self):
        self.ras.disconnect()


def main():
    """メイン"""
    if len(ad.CLIENT) < TARGET:
        print("len(address) < TARGET")
        raise ValueError()
    rass, threads = [], []
    for i in range(TARGET):
        ras = Connection(i)
        if ras.is_aivable():
            rass.append(ras)
            thread = threading.Thread(
                target=ras.main_process, args=([PERIOD]))
            threads.append(thread)

    for thread in threads:
        thread.start()

    for ras in rass:
        del ras


if __name__ == "__main__":
    main()
