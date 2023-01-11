"""
https://leetcode.com/problems/maximize-distance-to-closest-person/
"""
from typing import List

from src.utils import Timer


class Solution:
    def __init__(self):
        self.max_delta = 0
        self.max_delta_pos = None

    def update_max_delta(self, prev_seat_pos, seat_pos, seats):
        if prev_seat_pos == 0 and seats[0] == 0:
            prev_seat_pos = -seat_pos

        delta = seat_pos - prev_seat_pos
        if delta > self.max_delta:
            self.max_delta = delta
            self.max_delta_pos = prev_seat_pos

    def maxDistToClosest(self, seats: List[int]) -> int:
        prev_seat_pos = 0
        seat_pos = 0
        for seat_pos, sit in enumerate(seats):
            if sit:
                self.update_max_delta(prev_seat_pos, seat_pos, seats)
                prev_seat_pos = seat_pos

        if seat_pos > prev_seat_pos:
            seat_pos = seat_pos + (seat_pos - prev_seat_pos)
            self.update_max_delta(prev_seat_pos, seat_pos, seats)

        elif self.max_delta_pos == prev_seat_pos and seat_pos > prev_seat_pos:
            return self.max_delta
        return self.max_delta // 2


if __name__ == "__main__":
    timer = Timer()
    cases = [
        # (dict(seats=[1, 0, 0, 0, 1, 0, 1]), 2),
        (dict(seats=[1, 0, 0]), 2),
    ]

    for kwargs, expected_output in cases:
        output = Solution().maxDistToClosest(**kwargs)
        assert expected_output == output
    timer.calc_time()
