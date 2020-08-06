"""BT通信関連ライブラリ"""
# -*- coding: utf-8 -*-
from time import sleep
import bluetooth as bt


class Connect:
    """BT"""

    def __init__(self, name, addr, port):
        self.__name = name
        self.__bdaddr = addr
        self.__port = port
        self.__sock = bt.BluetoothSocket(bt.RFCOMM)

    @property
    def name(self):
        """名前"""
        return

    @name.getter
    def name(self):
        """getter"""
        return self.__name

    @name.setter
    def name(self, name):
        """setter"""
        self.__name = name

    @property
    def bdaddr(self):
        """bdaddr"""
        return

    @bdaddr.getter
    def bdaddr(self):
        """getter"""
        return self.__bdaddr

    @bdaddr.setter
    def bdaddr(self, value):
        """setter"""
        self.__bdaddr = value

    @property
    def port(self):
        """port"""
        return

    @port.getter
    def port(self):
        """getter"""
        return self.__port

    @port.setter
    def port(self, value):
        """setter"""
        self.__port = value

    @property
    def sock(self):
        """sock"""
        return

    @sock.getter
    def sock(self) -> bt.BluetoothSocket:
        """getter"""
        return self.__sock

    @sock.setter
    def sock(self, value):
        """setter"""
        self.__sock = value

    def reconnect(self, addr, num):
        """reconnect"""
        self.__bdaddr = addr
        self.__port = num
        self.__sock = bt.BluetoothSocket(bt.RFCOMM)

    def connectbluetooth(self, bdaddr, port) -> bool:
        """connect"""
        for _ in range(4):
            try:
                if isinstance(self.__sock, bt.BluetoothSocket):
                    self.__sock.connect((bdaddr, port))
                    sleep(2)
            except bt.BluetoothError:
                self.reconnect(bdaddr, port)
                sleep(0.5)
            except KeyboardInterrupt:
                break
            else:
                return True
        return False

    def disconnect(self):
        """disconnect"""
        self.__sock.close()
