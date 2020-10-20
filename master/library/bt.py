# -*- coding: utf-8 -*-
"""Basic Bluetooth Connection Library"""
import time
import bluetooth


class Bluetooth:
    """Basic Bluetooth Class"""

    def __init__(self):
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    def send(self, data: int, bit_size: int = 8):
        """Send int data"""
        self.sock.send((data).to_bytes(bit_size, "big"))

    def receive(self, bit_size: int = 8) -> int:
        """Receive int data"""
        return int.from_bytes(self.sock.recv(bit_size), "big")

    def disconnect(self):
        """Disconnect"""
        self.sock.close()

    def __del__(self):
        self.disconnect()


class BluetoothParent(Bluetooth):
    """Bluetooth Parent Class"""

    def __init__(self, port: int, address: str):
        super().__init__()
        self.__port = port
        self.__address = address

    def connect(self):
        """Connect device"""
        while True:
            try:
                self.sock.connect((self.__address, self.__port))
                time.sleep(0.25)
            except bluetooth.BluetoothError:
                self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            else:
                break


class BluetoothChild(Bluetooth):
    """Bluetooth Child Class"""

    def __init__(self, port: int, address: str = None):
        super().__init__()
        self.__port: int = port
        self.__address: str = address
        self.__binded: bluetooth.BluetoothSocket = None

    def connect(self):
        """Connect device"""
        self.sock.bind(("", self.__port))
        self.sock.listen(self.__port)
        if self.__address is None:
            self.sock = self.sock.accept()[0]
        else:
            self.__binded, self.sock = self.sock.accept()
            if self.__binded is not self.__address:
                self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                self.connect()


if __name__ == '__main__':
    pass
