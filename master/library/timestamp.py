# -*- coding: utf-8 -*-
"""タイムスタンプの管理"""
import time

class Timestamp:
    """タイムスタンプ"""
    time_stamp = 0
    def __init__(self, length: int):
        self.__length = length
        self.__aivable = [False for _ in range(length)]

    def change_ready(self, index: int):
        """準備ができたかどうかを変更する"""
        if index >= self.__length:
            raise ValueError("index >= TARGET")
        self.__aivable[index] = True

    def get_timestamp(self) -> int:
        """タイムスタンプを発行する"""
        if Timestamp.time_stamp == 0:
            if not False in self.__aivable:
                Timestamp.time_stamp = int((time.time()+2)*10000000)
        return Timestamp.time_stamp


if __name__ == "__main__":
    pass
