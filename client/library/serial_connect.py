# -*- coding: utf-8 -*-
"""シリアル通信"""
import serial
import struct


class Serial_Connection:
    """シリアル通信"""

    def __init__(self, port: str, rate: int) -> bool:
        try:
            self.connection = serial.Serial(port, rate)
        except serial.SerialException:
            return False
        if self.connection.aivable:
            return True

    def write(self, data: int):
        """送信"""
        self.connection.write(struct.pack("b", data))

    def read(self):
        """受信"""
        return self.connection.read()

    def __del__(self):
        self.connection.close()


if __name__ == "__main__":
    pass