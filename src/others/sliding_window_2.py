""" Exercise from https://www.youtube.com/watch?v=Z0iT7BZruYs&"""
from typing import List

import numpy as np

from src.utils import Timer


class Solution:
    def execute(self, persons: List, start_year: int, end_year: int):
        lives_index = np.zeros(end_year - start_year + 2, dtype=int)
        for birth, death in persons:
            lives_index[birth - start_year] += 1
            lives_index[death - start_year + 1] -= 1

        max_idx = 0
        max_lives = 0
        curr_lives = 0
        for i, lives in enumerate(lives_index):
            curr_lives += lives
            if curr_lives > max_lives:
                max_lives = curr_lives
                max_idx = i

        return start_year + max_idx


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (
            {
                "persons": [[1990, 2012], [1991, 1993], [1990, 1999], [1992, 2010], [1992, 2010]],
                "start_year": 1990,
                "end_year": 2012,
            },
            1992,
        ),
        (
            {
                "persons": [[1995, 2012], [1991, 1993], [1995, 1999], [1992, 2010], [1992, 2010]],
                "start_year": 1990,
                "end_year": 2012,
            },
            1995,
        ),
    ]
    for kwargs, expected_output in cases:
        output = Solution().execute(**kwargs)
        assert expected_output == output
    timer.calc_time()
