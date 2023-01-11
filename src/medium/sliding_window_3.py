"""
https://leetcode.com/problems/longest-repeating-character-replacement/
"""
from src.utils import Timer


class Solution:
    def add_to_dict(self, counts, letter):
        counts[letter] = 1 + counts.get(letter, 0)

    def max_count(self, counts):
        return counts[max(counts, key=counts.get)]

    def length(self, left_i, right_i):
        return right_i - left_i + 1

    def characterReplacement(self, s: str, k: int) -> int:
        left_i = 0
        max_len = 0
        counts = {}

        for right_i, letter in enumerate(s):
            self.add_to_dict(counts, letter)

            while self.length(left_i, right_i) - self.max_count(counts) > k:
                counts[s[left_i]] -= 1
                left_i += 1

            curr_len = self.length(left_i, right_i)
            if curr_len > max_len:
                max_len = curr_len

        return max_len


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (dict(s="AABABBBA", k=1), 5),
        (dict(s="ABAB", k=2), 4),
    ]
    for kwargs, expected_output in cases:
        output = Solution().characterReplacement(**kwargs)
        assert expected_output == output
    timer.calc_time()
