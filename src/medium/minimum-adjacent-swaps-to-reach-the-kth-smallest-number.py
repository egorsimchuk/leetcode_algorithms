"""
https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/description/
"""
import bisect
from itertools import combinations

import numpy as np


class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        wond_numbers_count, sorted_arr = self.get_wonderful_counts(num, k)
        wonderful_number = self.get_wonderful_number(sorted_arr, wond_numbers_count, k)
        res = self.get_n_swaps(num, wonderful_number)
        return res

    def get_wonderful_counts(self, num, k):
        reveresed_num = num[::-1]
        wond_numbers = 0
        used_number_pos = 0
        sorted_arr = []
        while wond_numbers < k:
            # update sorted arr
            sorted_arr_pos = self.update_sorted_arr(sorted_arr, int(reveresed_num[used_number_pos]))
            len_sorted_arr = len(sorted_arr)
            # skip if next number is equal to max (last) number in sorted_arr
            if sorted_arr_pos == len_sorted_arr:
                used_number_pos += 1
                continue

            # fetch sorted arr from new inserted to max (last)
            while sorted_arr_pos < len_sorted_arr:
                fetched_value = sorted_arr[sorted_arr_pos]
                wond_numbers += self.count_permutations(sorted_arr, sorted_arr_pos)
                # skip the same digits
                while sorted_arr_pos < len_sorted_arr and fetched_value == sorted_arr[sorted_arr_pos]:
                    sorted_arr_pos += 1

            used_number_pos += 1
        return int(wond_numbers), sorted_arr

    def update_sorted_arr(self, sorted_arr, used_number):
        bisect.insort(sorted_arr, used_number)
        sorted_arr_pos = bisect.bisect_right(sorted_arr, used_number)
        return sorted_arr_pos

    def count_permutations(self, sorted_arr, sorted_arr_pos):
        permutations_array = sorted_arr.copy()
        permutations_array.pop(sorted_arr_pos)

        a = self.count_simple_permutations(len(permutations_array))
        uniq = np.unique(permutations_array, return_counts=True)[1]
        b = 1
        for n in uniq[uniq > 1]:
            b *= self.count_simple_permutations(n)
        return a / b

    def count_simple_permutations(self, len):
        return np.prod(range(1, len + 1))

    def get_wonderful_number(self, sorted_arr, wond_numbers_count, k):
        extra_count = wond_numbers_count - k
        sorted_arr_inv = sorted_arr[::-1]
        sorted_arr_inv = [4, 3, 2, 2, 1]
        pos = len(sorted_arr_inv) - 1
        wonderful_numbers = []
        while True:
            sorted_arr_inv[pos]
            right_part = sorted_arr_inv[pos + 1:]
            if len(right_part) == 0:
                pos -= 1
                continue
            argmax = pos + 1 + np.argmax(right_part)
            sorted_arr_inv[pos], sorted_arr_inv[pos + 1] = sorted_arr_inv[argmax]
        return

    def get_n_swaps(self, from_num, to_num):
        return


if __name__ == '__main__':
    num = "5489355142"
    k = 3
    res = Solution().getMinSwaps(num, k)
    assert res == 4
