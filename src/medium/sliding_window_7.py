"""
https://www.lintcode.com/problem/883/
"""
from typing import List

from src.utils import Timer


class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """

    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        # write your code here
        max_l = 0
        flip_idx = None

        left = 0
        right = 0
        for right, n in enumerate(nums):
            if n == 1:
                pass
            elif flip_idx is None:
                if left == right:
                    left += 1
                else:
                    flip_idx = right
            else:
                curr_l = right - left
                if curr_l > max_l:
                    max_l = curr_l
                left = flip_idx + 1
                flip_idx = right

        curr_l = right - left
        if nums[right] == 1:
            curr_l += 1
        if curr_l > max_l:
            max_l = curr_l
        return max_l


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (dict(nums=[1, 0, 1, 0, 1, 1, 0, 0]), 4),
        (dict(nums=[1, 1, 0, 1, 1, 0, 0]), 5),
        (dict(nums=[0, 0, 0, 1, 1, 0, 1, 1, 0, 0]), 5),
        (dict(nums=[0, 1, 1, 0, 0, 0]), 3),
        (dict(nums=[1, 1, 1]), 3),
    ]

    for kwargs, expected_output in cases:
        output = Solution().find_max_consecutive_ones(**kwargs)
        assert expected_output == output
    timer.calc_time()
