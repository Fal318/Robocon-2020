# -*- coding: utf-8 -*-
"""PC側"""
import time
import threading
import bluetooth as bt
import address as ad
from library import bt_connect
from library import timestamp as ts

HOST_NAME = ["ukulele", "percussion"]
IS_DEBUG: bool = True  # デバッグ用かどうか
TARGET: int = 2  # TARGET:接続する台数
timestamp = ts.Timestamp(TARGET)


class Connection:
    """通信を定周期で行う"""
    STOP = False

    def __init__(self, proc_id: int):
        self.__proc_id: int = proc_id  # プロセスを識別するID

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

    def __send(self, data: int, size: int):
        """データ(整数値)を送信する"""
        self.__ras.sock.send((data).to_bytes(size, "little"))
        print("target={0} send:{1}".format(self.__proc_id, data))

    def __read(self):
        return int.from_bytes(
            self.__ras.sock.recv(1), "little")

    def main_process(self):
        """メインプロセス"""
        try:
            if not self.__read():
                raise Exception(f"{HOST_NAME[self.__proc_id]} was Failed")
            else:
                print(f"{time.time()}: {HOST_NAME[self.__proc_id]} is ready")
            timestamp.change_aivable(self.__proc_id)
            while not timestamp.get_timestamp():
                continue
            self.__send(timestamp.get_timestamp(), 64)
            self.__ras.set_timeout(0.1)
            while not Connection.STOP:
                try:
                    self.__read()
                except OSError:
                    continue
                else:
                    Connection.STOP = True
                    break
        except KeyboardInterrupt:
            self.__send(0, 1)
            print("Connection Killed")
        except bt.BluetoothError:
            print("Connection Killed")
        else:
            self.__send(0, 1)

    def get_status(self):
        self.__read()

    def __del__(self):
        self.__ras.disconnect()


def main():
    """メイン"""
    if len(ad.CLIENT) < TARGET:
        raise ValueError("len(address) < TARGET")
    ras_arr, threads = [], []
    for i in range(TARGET):
        ras = Connection(i)
        if ras.is_aivable():
            ras_arr.append(ras)
            threads.append(threading.Thread(target=ras.main_process))

    for thread in threads:
        thread.start()

    for ras in ras_arr:
        del ras


if __name__ == "__main__":
    main()
