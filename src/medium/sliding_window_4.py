"""
https://leetcode.com/problems/find-all-anagrams-in-a-string
"""
from typing import List


class Solution:
    def add_to_dict(self, d, letter):
        d[letter] = 1 + d.get(letter, 0)

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        req_dict = {}
        curr_dict = {}
        for i, p_val in enumerate(p):
            self.add_to_dict(req_dict, p_val)
            self.add_to_dict(curr_dict, s[i])

        left = 0
        res = []
        if req_dict == curr_dict:
            res.append(0)

        for sym in s[len(p) :]:  # noqa: E203
            self.add_to_dict(curr_dict, sym)
            curr_dict[s[left]] -= 1
            if curr_dict[s[left]] == 0:
                curr_dict.pop(s[left])
            left += 1

            if curr_dict == req_dict:
                res.append(left)
        return res


if __name__ == "__main__":
    import time

    start_time = time.time()
    cases = [
        (dict(s="aaaaaaaaaa", p="aaaaaaaaaaaaa"), []),
        (dict(s="cbaebabacd", p="abc"), [0, 6]),
    ]

    for kwargs, expected_output in cases:
        output = Solution().findAnagrams(**kwargs)
        assert expected_output == output

    print(f"Execution time: {round(time.time() - start_time, 3)} seconds")
