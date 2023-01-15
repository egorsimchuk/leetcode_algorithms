"""
https://leetcode.com/problems/group-anagrams
"""
from collections import defaultdict
from typing import List

from src.utils import Timer


class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    def groupAnagrams_v2(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}

        def calc_key(s):
            s_key = {}
            for sym in s:
                if sym in s_key:
                    s_key[sym] += 1
                else:
                    s_key[sym] = 1
            return tuple(sorted(s_key.items()))

        for s in strs:
            s_key = calc_key(s)
            if s_key in res_dict:
                res_dict[s_key].append(s)
            else:
                res_dict[s_key] = [s]

        result = []
        for s_list in res_dict.values():
            result.append(s_list)

        return result


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (dict(strs=["eat", "tea", "tan", "ate", "nat", "bat"]), [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
    ]
    for kwargs, expected_output in cases:
        output = Solution().groupAnagrams(**kwargs)
        assert expected_output == output
    timer.calc_time()
