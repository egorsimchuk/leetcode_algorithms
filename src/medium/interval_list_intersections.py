"""
https://leetcode.com/problems/interval-list-intersections/
"""
from typing import List

from src.utils import Timer


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        try:
            first = firstList[0]
            second = secondList[0]
        except IndexError:
            return []

        if firstList[0][0] > secondList[0][0]:
            return self.intervalIntersection(firstList=secondList, secondList=firstList)
        if firstList[0][0] == secondList[0][0] and firstList[0][1] < secondList[0][1]:
            return self.intervalIntersection(firstList=secondList, secondList=firstList)

        if first[1] < second[0]:  # pylint: disable=R1705
            firstList.pop(0)
            return self.intervalIntersection(firstList=secondList, secondList=firstList)
        elif first[0] < second[0] and second[0] <= first[1] and first[1] <= second[1]:
            firstList.pop(0)
            return [[second[0], first[1]]] + self.intervalIntersection(firstList=secondList, secondList=firstList)
        elif first[0] <= second[0] and second[0] <= first[1] and first[0] < second[1] and second[1] <= first[1]:
            secondList.pop(0)
            return [[second[0], second[1]]] + self.intervalIntersection(firstList=firstList, secondList=secondList)
        else:
            raise ValueError("Unexpected")


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (
            dict(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]], secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]),
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        ),
        (dict(firstList=[[1, 3], [5, 9]], secondList=[]), []),
        (dict(firstList=[[1, 3]], secondList=[[1, 3]]), [[1, 3]]),
    ]

    for kwargs, expected_output in cases:
        output = Solution().intervalIntersection(**kwargs)
        assert expected_output == output
    timer.calc_time()
