"""
https://leetcode.com/problems/minimum-window-substring/
"""
from src.utils import Timer


class Solution:
    def init_dict(self, t):
        req_counts = {}
        for sym in t:
            if sym in req_counts:
                req_counts[sym] += 1
            else:
                req_counts[sym] = 1
        return req_counts

    def update_start_i(self, counts_in_substring, req_counts, s, start_i):
        """Move start substring right unless it is possible"""
        while True:
            first_sym = s[start_i]
            if first_sym in counts_in_substring and counts_in_substring[first_sym] > req_counts[first_sym]:
                start_i += 1
                counts_in_substring[first_sym] -= 1
            elif first_sym not in counts_in_substring:
                start_i += 1
            else:
                break
        return start_i

    def is_find_all(self, counts_in_substring, req_counts):
        for sym, count in counts_in_substring.items():
            if count < req_counts[sym]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        req_counts = self.init_dict(t)
        counts_in_substring = {k: 0 for k in req_counts}

        start_i = 0
        min_l = 1e6
        min_window = [0, 0]
        for i, sym in enumerate(s):
            if sym not in counts_in_substring:
                continue
            counts_in_substring[sym] += 1
            start_i = self.update_start_i(counts_in_substring, req_counts, s, start_i)
            new_l = i - start_i + 1
            if self.is_find_all(counts_in_substring, req_counts) and new_l < min_l:
                min_l = new_l
                min_window = [start_i, i + 1]

        return s[slice(*min_window)]


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (dict(s="aabbbbbcdd", t="abcdd"), "abbbbbcdd"),
        (dict(s="ADOBECODEBANC", t="ABC"), "BANC"),
        (dict(s="a", t="a"), "a"),
        (dict(s="a", t="aa"), ""),
    ]
    for kwargs, expected_output in cases:
        output = Solution().minWindow(**kwargs)
        assert expected_output == output
    timer.calc_time()
