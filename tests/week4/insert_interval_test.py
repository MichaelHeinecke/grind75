import pytest

from grind75.week4.insert_interval import Solution


@pytest.mark.parametrize(
    "intervals, new_interval, expected_result",
    [
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
    ],
)
def test_new_interval_is_inserted_correctly(intervals, new_interval, expected_result):
    actual_result = Solution().insert(intervals, new_interval)
    assert actual_result == expected_result
