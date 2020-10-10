import time


class Lag:
    def __init__(self):
        self.__start_time = None
        self.__period = []

    def get_lag(self, period, send_time):
        if self.__start_time is None:
            self.__start_time = send_time
        self.__period.append(period)
        return self.__start_time + sum(self.__period) - time.time()
