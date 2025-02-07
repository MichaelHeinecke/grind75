import pytest

from grind75.week4.one_matrix import Solution


@pytest.mark.parametrize(
    "matrix, expected_result",
    [
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
        ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]),
        ([[0]], [[0]]),
    ],
)
def test_cell_distances_to_closest_0_cell_calculated_correctly(matrix, expected_result):
    actual_result = Solution().updateMatrix(expected_result)
    assert actual_result == expected_result
