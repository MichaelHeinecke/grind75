import pytest

from grind75.week4.squares_of_sorted_array import Solution


@pytest.mark.parametrize(
    "nums, expected_result",
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ],
)
def test_numbers_are_squared_and_sorted(nums: list[int], expected_result: list[int]):
    actual_result = Solution().sortedSquares(nums)
    assert actual_result == expected_result
