"""
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element
"""
from typing import List

from src.utils import Timer


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_deleted = False
        prev_zero_idx = None
        left = 0
        right = 0
        value = 0
        max_len = 0

        def update_max_len(max_len, left, right):
            new_len = right - left - 1
            if new_len > max_len:
                max_len = new_len
            return max_len

        for right, value in enumerate(nums):
            if value == 1:
                continue
            if value == 0 and prev_zero_idx == right - 1:
                max_len = update_max_len(max_len, left, right)
                left = right + 1
                zero_deleted = False
            elif value == 0 and not zero_deleted:
                prev_zero_idx = right
                zero_deleted = True
            elif value == 0 and zero_deleted:
                max_len = update_max_len(max_len, left, right)
                left = prev_zero_idx + 1
                prev_zero_idx = right
            else:
                raise ValueError("Not reachable")

        if zero_deleted:
            max_len = update_max_len(max_len, left, right + 1)
        elif left > 0 and nums[left - 1] == 0:
            max_len = update_max_len(max_len, left, right + 2)
        else:
            max_len = update_max_len(max_len, left, right + 1)

        return max_len

    def longestSubarrayFast(self, A):
        k = 1
        i = 0
        j = 0
        for j, value in enumerate(A):
            k -= value == 0
            if k < 0:
                k += A[i] == 0
                i += 1
        return j - i


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (dict(nums=[1, 0, 0]), 1),
        (dict(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]), 5),
        (dict(nums=[1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]), 11),
        (dict(nums=[1, 1, 0, 0, 1, 1, 1, 0, 1]), 4),
        (dict(nums=[1, 1, 0]), 2),
        (dict(nums=[1, 1, 1]), 2),
        (dict(nums=[0, 1, 1]), 2),
    ]

    for kwargs, expected_output in cases:
        output = Solution().longestSubarray(**kwargs)
        assert expected_output == output
    timer.calc_time()
