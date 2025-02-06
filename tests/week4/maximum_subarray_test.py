import pytest

from grind75.week4.maximum_subarray import Solution


@pytest.mark.parametrize(
    "nums, expected_result",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([0], 0),
        ([-1], -1),
        ([5, 4, -1, 7, 8], 23),
    ],
)
def test_maximum_subarray_sum_is_calculated_correctly(nums, expected_result):
    actual_result = Solution().maxSubArray(nums)
    assert actual_result == expected_result
