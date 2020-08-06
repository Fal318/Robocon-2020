"""クライアント側"""
import sys
import csv
import time
import bluetooth as bt
import address as ad
from library import connect


args = sys.argv
if len(args) != 2:
    print("ポート番号を引数で入力してください")
    sys.exit(1)
PORT = int(args[1])


class Connection:
    """通信関連のクラス"""

    def __init__(self):
        self.data = None
        self.file = None
        self.sendtime = None
        self.recv_data = []
        self.send_data = []
        self.ras = connect.Connect("sev", ad.SERVER, PORT)
        while True:
            if self.ras.connectbluetooth(self.ras.bdaddr, self.ras.port):
                break

    def send(self, value):
        """データ(整数値)を送信する関数"""
        self.data = value
        self.sendtime = time.time()
        self.ras.sock.send((self.data).to_bytes(1, "little"))
        self.send_data.append([time.time(), self.data])
        print("send:{0}".format(self.data))

    def receive(self):
        """データを受信する関数"""
        self.data = int.from_bytes(self.ras.sock.recv(1024), "little")
        self.recv_data.append([time.time(), self.data])
        print("host:{0} recv:{1}".format("server", self.data))

    def write_logs(self):
        """送受信のログをcsvに書き込む関数"""
        self.file = open(f"../log/cdata{PORT-1}.csv", "w")
        csv.writer(self.file).writerows(self.recv_data)
        self.file.close()

    def __del__(self):
        self.write_logs()
        self.ras.disconnect()


def main():
    """メイン"""
    ras = Connection()
    while True:
        try:
            ras.receive()
        except bt.BluetoothError:
            break
    del ras


if __name__ == '__main__':
    main()
