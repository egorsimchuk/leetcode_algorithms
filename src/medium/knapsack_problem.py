"""
https://leetcode.com/problems/ones-and-zeroes/description/
"""
from typing import List

import numpy as np


class Solution:
    def __init__(self):
        self.num = None

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        weights = [[s.count("0"), s.count("1")] for s in strs]
        matrix = self.get_matrix2(None, weights, (m, n))
        print(f"weights:\n{weights}")
        print(f"matrix:\n{matrix}")
        return matrix[-1, -1]

    def get_matrix2(self, scores, weights, capacity):
        matrix_shape = [c + 1 for c in capacity]
        matrix = np.zeros(matrix_shape, dtype=int)
        for a, b in weights:
            for i in range(capacity[0], a - 1, -1):
                for j in range(capacity[1], b - 1, -1):
                    matrix[i, j] = max(matrix[i, j], matrix[i - a, j - b] + 1)
        return matrix


if __name__ == "__main__":
    import time

    start_time = time.time()
    cases = [
        ({"strs": ["10", "0001", "111001", "1", "0"], "m": 5, "n": 3}, 4),
    ]

    for kwargs, expected_output in cases:
        output = Solution().findMaxForm(**kwargs)
        assert expected_output == output

    print(f"Execution time: {round(time.time()-start_time,3)} seconds")
