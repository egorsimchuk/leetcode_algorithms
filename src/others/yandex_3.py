import time


class Solution:
    def execute(self, games):
        return ""


if __name__ == "__main__":

    start_time = time.time()
    cases = [
        (
            {"games": ["Linux - Gentoo - 1:0", "Gentoo - Windows - 2:1", "Linux - Windows - 0:2"]},
            "+-+--------+-+-+-+-+-+\n|1|Gentoo  |X|L|W|3|1|\n+-+--------+-+-+-+-+-+\n|2|Linux   |W|X|L|3|1|\n+-+--------+-+-+-+-+-+\n|3|Windows |L|W|X|3|1|\n+-+--------+-+-+-+-+-+",
        ),
    ]

    for kwargs, expected_output in cases:
        output = Solution().execute(**kwargs)
        assert expected_output == output

    print(f"Execution time: {round(time.time()-start_time,3)} seconds")
