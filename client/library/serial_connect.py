# -*- coding: utf-8 -*-
"""シリアル通信"""
import serial


STOP_BYTE = [b'\x01', b'\x01', b'\x01', b'\x01', b'\x00']


class Serial_Connection:
    """シリアル通信"""

    def __init__(self, port: str, rate: int) -> bool:
        try:
            self.__connection = serial.Serial(port, rate)
            self.__aivable = True
        except serial.SerialException:
            self.__aivable = False
            print("Serial Connection Failed")
        else:
            print("Serial Device is Connected")

    def write(self, data: bytes):
        self.__connection.write(data)

    def is_aivable(self):
        return self.__aivable

    def __del__(self):
        if self.__aivable:
            for b in STOP_BYTE:
                self.write(b)
            self.__connection.close()


if __name__ == "__main__":
    pass
