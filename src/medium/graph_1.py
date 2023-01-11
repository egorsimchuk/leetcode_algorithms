"""
https://leetcode.com/problems/path-with-minimum-effort
Used Dijkstra’s Shortest Path Algorithm https://www.youtube.com/watch?v=pVfj6mxhdMw
"""
from typing import List

import numpy as np

from src.utils import Timer


class Solution:
    def __init__(self):
        self.y_idx_max = None
        self.x_idx_max = None

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heights = np.array(heights)
        # vertexes = [(n, i) for n in range(heights.shape[0]) for i in range(heights.shape[1])]
        self.y_idx_max = heights.shape[0]
        self.x_idx_max = heights.shape[1]

        dist_from_root = np.zeros_like(heights, dtype=float)
        dist_from_root[:] = np.inf
        prev_vertex = np.zeros_like(heights, dtype=object)
        dist_from_root[0, 0] = 0

        unvisited_mask = np.ones_like(heights, dtype=bool)
        moves = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        while np.sum(unvisited_mask) > 0:
            visit_idx = np.argmin(dist_from_root[unvisited_mask])
            visit_idx = tuple(idxs[visit_idx] for idxs in np.where(unvisited_mask))
            visit_height = heights[visit_idx]
            visit_dist_from_root = dist_from_root[visit_idx]
            for x, y in moves:
                move_idx = (visit_idx[0] + y, visit_idx[1] + x)
                if not self.is_possible_move(move_idx):
                    continue
                move_distance = max(visit_dist_from_root, abs(heights[move_idx] - visit_height))
                if move_distance < dist_from_root[move_idx]:
                    prev_vertex[move_idx] = visit_idx
                    dist_from_root[move_idx] = move_distance

            unvisited_mask[visit_idx] = False
        return int(dist_from_root[-1, -1])

    def is_possible_move(self, move_idx):
        if 0 <= move_idx[0] < self.y_idx_max and 0 <= move_idx[1] < self.x_idx_max:
            return True
        return False


if __name__ == "__main__":
    timer = Timer()
    cases = [
        ({"heights": [[1, 2, 2], [3, 8, 2], [5, 3, 5]]}, 2),
        ({"heights": [[1, 2, 2], [3, 8, 2], [5, 3, 5]]}, 2),
        ({"heights": [[1, 2, 3], [3, 8, 4], [5, 3, 5]]}, 1),
    ]
    for kwargs, expected_output in cases:
        output = Solution().minimumEffortPath(**kwargs)
        assert expected_output == output
    timer.calc_time()
