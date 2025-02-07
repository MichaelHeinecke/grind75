import pytest

from grind75.week4.three_sum import Solution


@pytest.mark.parametrize(
    "nums, expected_result",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ],
)
def test_binary_tree_level_order_traversal(nums, expected_result):
    actual_result = Solution().threeSum(nums)
    assert actual_result == expected_result
