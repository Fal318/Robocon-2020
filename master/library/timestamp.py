import time

class Timestamp:
    time_stamp = 0
    def __init__(self, length: int):
        self.__length = length
        self.__aivable = [False for _ in range(length)]
        self.ts: int = 0

    def change_aivable(self, index: int):
        if index >= self.__length:
            raise ValueError("index >= TARGET")
        self.__aivable[index] = True

    def get_timestamp(self) -> int:
        if Timestamp.time_stamp == 0:
            if not False in self.__aivable:
                Timestamp.time_stamp = int((time.time()+2)*10000000)
        return Timestamp.time_stamp


if __name__ == "__main__":
    pass
