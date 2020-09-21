# -*- coding: utf-8 -*-
"""送信側のプログラム"""
import sys
import time
import threading
import bluetooth as bt
import address as ad
from library import bt_connect
from library import fix_lag


args = sys.argv
IS_DEBUG = False
if len(args) > 1 and args[1] == "-d":
    IS_DEBUG = True


TARGET: int = 2
PERIOD: float = 0.1
LONG: int = 1000
"""
TARGET:接続する台数
PERIOD:実行周期(sec)
id:
    0:ウクレレ
    1:パーカッション
"""

fix_lag = fix_lag.FixLag()


class Connection:
    """通信を定周期で行う"""

    def __init__(self, proc_id: int):
        self.__send_data: list = list(range(LONG))  # 送るデータ
        self.__sendtime: float = None  # 最後に送信をした時間
        self.__proc_id: int = proc_id  # プロセスを識別するID
        self.__lag: int = 0
        self.__ended: bool = False

        try:
            # 通信用のインスタンスを生成
            self.__ras = bt_connect.Connect("ras{0}".format(
                self.__proc_id), ad.CLIENT[self.__proc_id], 1, IS_DEBUG)

            if self.__ras.connectbluetooth(self.__ras.bdaddr, self.__ras.port):
                self.__aivable = True
                print("Connect")
            else:
                self.__aivable = False
                print("Connection Failed")
        except IndexError:
            self.__aivable = False

    def is_aivable(self) -> bool:
        """プロセスが有効かどうかを返す"""
        return self.__aivable

    def send(self, data: int):
        """データ(整数値)を送信する"""
        self.__sendtime = time.time()
        self.__ras.sock.send((data).to_bytes(1, "little"))
        print("target={0} send:{1}".format(self.__proc_id, data))

    def read(self):
        """データの受信"""
        fix_lag.add(self.__proc_id, int.from_bytes(
            self.__ras.sock.recv(64), "little")/10000000)

    def main_process(self, period: int):
        """メインプロセス"""
        try:
            for send in self.__send_data[0]:
                self.send(send)
                time.sleep(period - (time.time() - self.__sendtime)+self.__lag)
        except KeyboardInterrupt:
            self.send(0)
            print("Connection Killed")
        except ValueError:
            self.send(0)
            print("周期が早すぎます")
        except bt.BluetoothError:
            print("Connection Killed")
        else:
            self.send(0)
        finally:
            self.__ended = True

    def change_lag(self):
        """ラグの変更"""
        while not self.__ended:
            time.sleep(1)
            self.__lag = fix_lag.get_lag(self.__proc_id) / 10
            # 10ループ(1sec)で修正するので10で割る

    def __del__(self):
        self.__ras.disconnect()


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
    for ras in rass:
        thread = threading.Thread(target=ras.change_lag)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for ras in rass:
        del ras


if __name__ == "__main__":
    main()
