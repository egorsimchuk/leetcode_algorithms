"""
https://leetcode.com/problems/permutation-in-string/
"""
from src.utils import Timer


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def add_to_dict(d, sym):
            if sym in d:
                d[sym] += 1
            else:
                d[sym] = 1

        def remove_from_dict(d, sym):
            if d[sym] == 1:
                d.pop(sym)
            else:
                d[sym] -= 1

        expected_dict = {}
        for sym in s1:
            add_to_dict(expected_dict, sym)

        def is_bad(curr_dict, expected_dict):
            for sym, count in curr_dict.items():
                if sym not in expected_dict or count > expected_dict[sym]:
                    return True
            return False

        left = 0
        curr_dict = {}
        for sym in s2:
            if curr_dict == expected_dict:
                return True
            add_to_dict(curr_dict, sym)

            if is_bad(curr_dict, expected_dict):
                remove_from_dict(curr_dict, s2[left])
                left += 1

        if curr_dict == expected_dict:
            return True
        return False


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (dict(s1="ab", s2="iab"), True),
        (dict(s1="adc", s2="dcda"), True),
    ]

    for kwargs, expected_output in cases:
        output = Solution().checkInclusion(**kwargs)
        assert expected_output == output
    timer.calc_time()
