""" Exercise from https://habr.com/ru/company/yandex/blog/340784/ """

import numpy as np

from src.utils import Timer


class Solution:
    def execute(self):
        for n in range(1, 100):
            if self.is_comlex(n):
                return n

        raise ValueError("Not found")

    def is_comlex(self, n):
        for k in range(1, 100000):
            s_k = np.sum([int(x) for x in str(k)])
            if 3 * k / s_k ** 2 == n:
                return False
        return True


if __name__ == "__main__":
    timer = Timer()
    output = Solution().execute()
    assert output == 61
    timer.calc_time()
