"""
https://www.lintcode.com/problem/640/
"""
from src.utils import Timer


class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """

    def __init__(self):
        self.s_len = None
        self.t_len = None

    def is_one_edit_distance(self, s: str, t: str) -> bool:
        self.s_len = len(s)
        self.t_len = len(t)

        if self.s_len + self.t_len == 1:
            return True
        if abs(self.s_len - self.t_len) > 1:
            return False

        diff_count = 0
        s_i = 0
        t_i = 0
        while diff_count < 2:
            try:
                if s[s_i] != t[t_i]:
                    diff_count += 1
            except (IndexError, TypeError):
                break
            s_i, t_i = self.find_next_coordinates(s, t, s_i, t_i)
        return diff_count == 1

    def find_next_coordinates(self, s, t, s_i, t_i):
        possible_moves = [(1, 1), (1, 0), (0, 1)]
        s_next, t_next = None, None
        for s_mv, t_mv in possible_moves:
            try:
                if s[s_i + s_mv] == t[t_i + t_mv]:
                    s_next, t_next = s_i + s_mv, t_i + t_mv
            except IndexError:
                continue

        if s_next is None:
            for s_mv, t_mv in possible_moves:
                s_new = s_i + s_mv
                t_new = t_i + t_mv
                if s_new < self.s_len and t_new < self.t_len:
                    s_next, t_next = s_new, t_new
                    break

        return s_next, t_next


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (dict(s="a", t="ab"), True),
        (dict(s="", t=""), False),
        (dict(s="bcde", t="abcde"), True),
        (dict(s="b", t="a"), True),
    ]

    for kwargs, expected_output in cases:
        output = Solution().is_one_edit_distance(**kwargs)
        assert expected_output == output
    timer.calc_time()
