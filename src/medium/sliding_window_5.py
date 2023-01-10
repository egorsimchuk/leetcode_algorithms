"""
https://leetcode.com/problems/sliding-window-maximum/
"""
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        frame_idxs = deque()
        res = []

        for new_idx, new_value in enumerate(nums):
            while frame_idxs and new_value > nums[frame_idxs[-1]]:
                frame_idxs.pop()
            frame_idxs.append(new_idx)
            if frame_idxs[0] == new_idx - k:
                frame_idxs.popleft()
            res.append(nums[frame_idxs[0]])
        return res[k - 1 :]


if __name__ == "__main__":
    import time

    start_time = time.time()
    cases = [
        (dict(nums=[1, 3, -2, 0, -1, 3, 6, 7], k=3), [3, 3, 0, 3, 6, 7]),
        (dict(nums=[1], k=1), [1]),
    ]

    for kwargs, expected_output in cases:
        output = Solution().maxSlidingWindow(**kwargs)
        assert expected_output == output

    print(f"Execution time: {round(time.time() - start_time, 3)} seconds")
