"""
https://leetcode.com/problems/move-zeroes/
"""
from typing import List

from src.utils import Timer


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ancor = 0
        for i, n in enumerate(nums):
            if n != 0:
                nums[i], nums[ancor] = nums[ancor], nums[i]
                ancor += 1
        return nums


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (dict(nums=[0, 1, 0, 3, 12]), [1, 3, 12, 0, 0]),
        (dict(nums=[1, 0]), [1, 0]),
        (dict(nums=[0, 0, 1]), [1, 0, 0]),
    ]
    for kwargs, expected_output in cases:
        output = Solution().moveZeroes(**kwargs)
        assert expected_output == output
    timer.calc_time()
