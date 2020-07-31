# -*- coding: utf-8 -*-
from time import sleep
import bluetooth as bt


class Connect:
    def __init__(self, name, addr, num):
        self.__name = name
        self.__bdAddr = addr
        self.__port = num
        self.__sock = bt.BluetoothSocket(bt.RFCOMM)

    @property
    def name(self):
        pass

    @name.getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def bdAddr(self):
        pass

    @bdAddr.getter
    def bdAddr(self):
        return self.__bdAddr

    @bdAddr.setter
    def bdAddr(self, value):
        self.__bdAddr = value
        return

    @property
    def port(self):
        pass

    @port.getter
    def port(self):
        return self.__port

    @port.setter
    def port(self, value):
        self.__port = value
        return

    @property
    def sock(self):
        pass

    @sock.getter
    def sock(self):
        return self.__sock

    @sock.setter
    def sock(self, value):
        self.__sock = value

    def reConnect(self, addr, num):
        self.__bdAddr = addr
        self.__port = num
        self.__sock = bt.BluetoothSocket(bt.RFCOMM)

    def connectBluetooth(self, bdAddr, port):
        for _ in range(4):
            try:
                if type(self.__sock) == bt.BluetoothSocket:
                    self.__sock.connect((bdAddr, port))
                    sleep(2)
            except bt.BluetoothError:
                self.reConnect(bdAddr, port)
                sleep(0.5)
            except KeyboardInterrupt:
                break
            else:
                return True
        return False

    def disConnect(self, sock=None):
        self.__sock.close()
