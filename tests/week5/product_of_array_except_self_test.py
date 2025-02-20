import pytest

from grind75.week5.product_of_array_except_self import Solution


@pytest.mark.parametrize(
    "nums, expected_result",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ],
)
def test_notation_is_evaluated_correctly(nums, expected_result):
    actual_result = Solution().productExceptSelf(nums)
    assert actual_result == expected_result
