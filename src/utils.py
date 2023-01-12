"""Calculate execution time"""
from time import time


class Timer:
    def __init__(self, nround=3):
        self.start_time = time()
        self._nround = nround

    def calc_time(self):
        print(f"Execution time: {round(time() - self.start_time, self._nround)} seconds")
