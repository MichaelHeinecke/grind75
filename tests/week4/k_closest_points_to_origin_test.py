import pytest

from grind75.week4.k_closest_points_to_origin import Solution


@pytest.mark.parametrize(
    "points, k, expected_result",
    [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
    ],
)
def test_k_closest_points_are_returned(points, k, expected_result):
    actual_result = Solution().kClosest(points, k)
    assert actual_result == expected_result
