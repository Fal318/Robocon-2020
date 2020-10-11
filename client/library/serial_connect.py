# -*- coding: utf-8 -*-
"""シリアル通信"""
import serial
from cobs import cobs


def generate_cobs(value: int, byte_size: int) -> bytes:
    encoded = cobs.encode(value.to_bytes(byte_size, "big"))+b'\x00'
    return [encoded[i:i+1] for i in range(byte_size+2)]


class Connection:
    """シリアル通信"""

    def __init__(self, dev: str, rate: int, data_size: int) -> bool:
        try:
            self.__connection = serial.Serial(dev, rate)
            self.__data_size = data_size
            self.__aivable = True

        except serial.SerialException:
            self.__aivable = False
            print("Serial Connection Failed")
        else:
            print("Serial Device is Connected")

    def write(self, data: int):
        for gen_data in generate_cobs(data, self.__data_size):
            self.__connection.write(gen_data)

    def is_aivable(self):
        return self.__aivable

    def __del__(self):
        if self.__aivable:
            self.write(0)
            self.__connection.close()


if __name__ == "__main__":
    pass
