""" Exercise from https://habr.com/ru/company/yandex/blog/340784/ """
import numpy as np

from src.utils import Timer


class Solution:
    def execute(self, cards: str):
        arr = list(np.array(cards.split(" "), dtype=int))
        pet_sum = 0
        pet_card = arr.pop(0)
        vas_sum = 0
        vas_card = arr.pop(0)
        for card in arr:
            if pet_card < vas_card:
                pet_sum += pet_card
                pet_card = card
            else:
                vas_sum += vas_card
                vas_card = card

        # add last in hands cards
        pet_sum += pet_card
        vas_sum += vas_card
        if pet_sum < vas_sum:
            return "Vasya"
        return "Petya"


if __name__ == "__main__":
    timer = Timer()
    cases = [
        ({"cards": "1 2 3"}, "Petya"),
        ({"cards": "1 4 2"}, "Vasya"),
    ]
    for kwargs, expected_output in cases:
        output = Solution().execute(**kwargs)
        assert expected_output == output
    timer.calc_time()
