"""
https://leetcode.com/problems/number-of-islands
"""
from typing import List

from src.utils import Timer


class Solution:
    def __init__(self):
        self.i_len = None
        self.j_len = None

    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        n_islands = 0
        self.i_len = len(grid)
        self.j_len = len(grid[0])
        for i in range(self.i_len):
            for j in range(self.j_len):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    n_islands += 1
        return n_islands

    def dfs(self, grid, i, j):
        if i < 0 or i >= self.i_len or j < 0 or j >= self.j_len or grid[i][j] != "1":
            return
        grid[i][j] = "5"
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (
            dict(
                grid=[["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "1"]]
            ),
            2,
        ),
    ]

    for kwargs, expected_output in cases:
        output = Solution().numIslands(**kwargs)
        assert expected_output == output
    timer.calc_time()
