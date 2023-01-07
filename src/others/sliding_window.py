""" Exercise from https://www.youtube.com/watch?v=MCriLqc_8sY """
import time
from typing import List

import numpy as np


class Solution:
    def execute(self, numbers: List[int]):
        start_i = 0
        best_set = [-np.inf, 0, 0]
        curr_sum = 0

        for i, n in enumerate(numbers):
            curr_sum += n

            if curr_sum < 0:
                curr_sum = 0
                start_i = i + 1
            elif curr_sum > best_set[0]:
                best_set = [curr_sum, start_i, i + 1]

        if np.isinf(best_set[0]):
            idx_max = np.argmax(numbers)
            return [numbers[idx_max], idx_max, idx_max + 1]

        return best_set


if __name__ == "__main__":

    start_time = time.time()
    cases = [
        ({"numbers": [2, -1, 3, -2, 5, -1]}, [7, 0, 5]),
        ({"numbers": [2, -3, 3, -2, 5, -1]}, [6, 2, 5]),
        ({"numbers": [-2, -1]}, [-1, 1, 2]),
    ]

    for kwargs, expected_output in cases:
        output = Solution().execute(**kwargs)
        assert expected_output == output

    print(f"Execution time: {round(time.time() - start_time, 3)} seconds")
