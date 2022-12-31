import time


class Solution:
    def execute(self, bags, coins):

        return ""


if __name__ == "__main__":

    start_time = time.time()
    cases = [
        ({"bags": [2, 3], "coins": 5}, False),
        ({"bags": [2, 3], "coins": 3}, True),
    ]

    for kwargs, expected_output in cases:
        output = Solution().execute(**kwargs)
        assert expected_output == output

    print(f"Execution time: {round(time.time()-start_time,3)} seconds")
