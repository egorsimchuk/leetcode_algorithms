"""
https://leetcode.com/problems/cheapest-flights-within-k-stops
Used Dijkstra’s Shortest Path Algorithm https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Using_a_priority_queue
"""
import collections
import heapq
from typing import List

from src.utils import Timer


class Solution:
    def findCheapestPrice(self, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = collections.defaultdict(list)
        for a, b, p in flights:
            f[a].append([b, p])
        heap = [(0, src, k + 1)]
        city_stops = {}
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if i in city_stops and city_stops[i] >= k:
                # We already visited city but with less remaining stops. This way will be more expensive,
                # because we know that first heappop have smallest price for the destination. Skip for time saving
                continue
            city_stops[i] = k

            if k > 0:
                for v, v_price in f[i]:
                    heapq.heappush(heap, (p + v_price, v, k - 1))

        return -1


if __name__ == "__main__":
    timer = Timer()
    cases = [
        (dict(flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src=0, dst=3, k=2), 400),
        (dict(flights=[[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], src=0, dst=3, k=1), 6),
    ]
    for kwargs, expected_output in cases:
        output = Solution().findCheapestPrice(**kwargs)
        assert expected_output == output
    timer.calc_time()
