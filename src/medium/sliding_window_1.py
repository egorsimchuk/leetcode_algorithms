"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

from src.utils import Timer


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = set()
        start_i = 0
        max_l = 0
        for sym in s:
            while sym in sub_s:
                sub_s.remove(s[start_i])
                start_i += 1
            sub_s.add(sym)
            curr_l = len(sub_s)
            if curr_l > max_l:
                max_l = curr_l
        return max_l


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (dict(s="abcabcbb"), 3),
    ]
    for kwargs, expected_output in cases:
        output = Solution().lengthOfLongestSubstring(**kwargs)
        assert expected_output == output
    timer.calc_time()
