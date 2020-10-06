import time

timestamp = 0
class Timestamp:
    def __init__(self, length: int):
        self.__length = length
        self.__aivable = [False for _ in range(length)]
        self.ts: int = 0

    def change_aivable(self, index: int):
        if index >= self.__length:
            raise ValueError("index >= TARGET")
        self.__aivable[index] = True

    def get_timestamp(self) -> int:
        if not timestamp:
            if not False in self.__aivable:
                timestamp = int((time.time()+2)*10000000)
        return timestamp


if __name__ == "__main__":
    pass
