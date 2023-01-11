"""
https://leetcode.com/problems/summary-ranges/
"""
from typing import List

from src.utils import Timer


class Solution:
    def append_pair(self, res, left, prev_r):
        if left == prev_r:
            res.append(str(left))
        else:
            res.append(f"{left}->{prev_r}")

    def summaryRanges(self, nums: List[int]) -> List[str]:
        try:
            left = nums[0]
        except IndexError:
            return []
        prev_r = left
        res = []
        for r in nums[1:]:
            if r - prev_r > 1:
                self.append_pair(res, left, prev_r)
                left = r
            prev_r = r
        self.append_pair(res, left, prev_r)
        return res


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (dict(nums=[0, 1, 2, 4, 5, 7]), ["0->2", "4->5", "7"]),
        (dict(nums=[0, 2, 3, 4, 6, 8, 9]), ["0", "2->4", "6", "8->9"]),
    ]
    for kwargs, expected_output in cases:
        output = Solution().summaryRanges(**kwargs)
        assert expected_output == output
    timer.calc_time()
