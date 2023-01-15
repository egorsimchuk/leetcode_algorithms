"""
https://leetcode.com/problems/reverse-words-in-a-string-iii
"""


from src.utils import Timer


class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = 0

        def reverse(left, right):
            return s[left:right][::-1]

        res = []
        for right, sym in enumerate(s):
            if sym == " ":
                res.append(reverse(left, right))
                left = right + 1

        res.append(reverse(left, right + 1))

        res = " ".join(res)
        return res


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (dict(s="God Ding"), "doG gniD"),
    ]
    for kwargs, expected_output in cases:
        output = Solution().reverseWords(**kwargs)
        assert expected_output == output
    timer.calc_time()
