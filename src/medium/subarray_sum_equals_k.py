"""
https://leetcode.com/problems/subarray-sum-equals-k
"""
from collections import defaultdict
from typing import List

from src.utils import Timer


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        pref_sum_dict = defaultdict(int)
        pref_sum_dict[0] = 1
        res = 0
        cum_sum = 0
        for n in nums:
            cum_sum += n
            delta = cum_sum - k
            if delta in pref_sum_dict:
                res += pref_sum_dict[delta]
            pref_sum_dict[cum_sum] += 1
        return res


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (dict(nums=[1, 2, 3], k=3), 2),
    ]
    for kwargs, expected_output in cases:
        output = Solution().subarraySum(**kwargs)
        assert expected_output == output
    timer.calc_time()
