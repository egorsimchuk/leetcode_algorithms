"""
https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/description/
"""
import bisect
import itertools

import numpy as np


class Solution:
    def __init__(self):
        self.num = None

    def getMinSwaps(self, num: str, k: int) -> int:
        self.num = num
        wond_numbers_count, sorted_arr = self.get_wonderful_counts(k)
        wonderful_number = self.get_wonderful_number(sorted_arr, wond_numbers_count, k)
        res = self.get_n_swaps(wonderful_number)
        return res

    def get_wonderful_counts(self, k):
        reveresed_num = self.num[::-1]
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
            # Imagine we had [0 1 3 3 5] sorted_arr with new inserted value 1.
            # It means that it gave us a lot of new possibilities how to build wonderful number
            # We are trying to set bigger digits in old place of 1 one by one and count permutations,
            # we know that such number are bigger that with old 1 position
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

    def count_simple_permutations(self, n):
        return np.prod(range(1, n + 1))

    def get_wonderful_number(self, sorted_arr, wond_numbers_count, k):
        extra_count = wond_numbers_count - k
        right_part = self.get_biggest_n_combination(sorted_arr[::-1], extra_count)
        return self.num[: -len(sorted_arr)] + right_part

    def get_biggest_n_combination(self, sorted_arr_inv, extra_count):
        """
        Input: sorted_arr_inv = [4, 3, 2, 2, 1], extra_count = 2
        Output: '43122'
        """
        if extra_count == 0:
            return nums_to_string(sorted_arr_inv)
        combinations_set = {nums_to_string(arr) for arr in itertools.permutations(sorted_arr_inv)}
        return sorted(combinations_set)[-1 - extra_count]

    def get_n_swaps(self, to_num_str):
        """Get minimal number swaps from self.num to to_num"""
        from_num = list(self.num)
        to_num = list(to_num_str)
        cursor = 0
        n_swaps = 0
        while cursor < len(to_num):
            if from_num[cursor] == to_num[cursor]:
                cursor += 1
            else:
                nearest_pos = self.get_nearest_right_pos(from_num, to_num[cursor], cursor)
                self.swap_digits(from_num, nearest_pos, cursor)
                n_swaps += nearest_pos - cursor
                cursor += 1
        if from_num != to_num:
            raise ValueError(f"Numbers should be equall, got {from_num}, {to_num}")
        return n_swaps

    def get_nearest_right_pos(self, number, digit, cursor):
        return cursor + np.argmax(np.asarray(number[cursor:]) == digit)

    def swap_digits(self, number, pos_1, pos_2):
        if pos_2 >= pos_1:
            raise ValueError("pos_1 should be right to pos_2")
        return number.insert(pos_2, number.pop(pos_1))


def nums_to_string(arr):
    return "".join(np.asarray(arr, dtype="str"))


if __name__ == "__main__":
    cases = [
        ({"num": "32029466933338833", "k": 558}, 9),
        ({"num": "11112", "k": 4}, 4),
        ({"num": "059", "k": 5}, 3),
    ]

    for kwargs, expected_output in cases:
        output = Solution().getMinSwaps(**kwargs)
        assert expected_output == output
