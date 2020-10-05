# -*- coding: utf-8 -*-
"""シリアル通信"""
import serial
import struct


class Serial_Connection:
    """シリアル通信"""

    def __init__(self, port: str, rate: int) -> bool:
        try:
            self.__connection = serial.Serial(port, rate)
        except serial.SerialException:
            print("Serial Connection Failed")

    def write(self, data: int):
        """送信"""
        self.__connection.write(struct.pack("b", data))

    def read(self):
        """受信"""
        return self.c__onnection.read()

    def __del__(self):
        if self.__connection.aivable:
            self.write(0)
        self.__connection.close()


if __name__ == "__main__":
    pass
