# -*- coding: utf-8 -*-
"""複数台での通信の誤差修正"""


class Data:
    """最大要素を固定したスタックみたいな物"""

    def __init__(self, max_length: int):
        self.__array = []
        self.__max_length = max_length

    def add_data(self, data):
        """要素の追加"""
        if self.full():
            self.__remove_data()
        self.__array.append(data)

    def full(self) -> bool:
        """要素数が最大値を超えていないかを返す"""
        if len(self.__array) >= self.__max_length:
            return True
        return False

    def __remove_data(self):
        """先頭要素の削除"""
        del self.__array[0]

    def array_mean(self) -> float:
        """平均を返す"""
        return sum(self.__array) / len(self.__array)


class FixLag:
    """通信のラグを修正"""

    def __init__(self, max_length: int):
        self.__lag = 0
        self.__data = [Data(max_length) for _ in range(2)]

    def add(self, index: int, data: float):
        """要素の追加"""
        if index >= 2:
            raise IndexError("Id out of range")
        self.__data[index].add_data(data)

    def __call(self) -> float:
        """平均誤差の計算"""
        return sum([d.array_mean() for d in self.__data]) / 2

    def fix(self) -> list:
        """誤差を返す"""
        self.__lag = self.__call() / 2
        if self.__lag >= 0:
            return [-self.__lag, self.__lag]

        return [self.__lag, -self.__lag]


if __name__ == "__main__":
    pass
