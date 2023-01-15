"""
https://leetcode.com/problems/generate-parentheses
"""
from typing import List

from src.utils import Timer


class Solution:
    def generate(self, prev_str, left_count, right_count, parents):
        if left_count:
            self.generate(prev_str + "(", left_count - 1, right_count, parents)
        if right_count > left_count:
            self.generate(prev_str + ")", left_count, right_count - 1, parents)
        if right_count == 0:
            parents.append(prev_str)

        return parents

    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate("", n, n, [])


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (dict(n=3), ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    ]
    for kwargs, expected_output in cases:
        output = Solution().generateParenthesis(**kwargs)
        assert expected_output == output
    timer.calc_time()
