import pytest

from grind75.week5.number_of_islands import Solution


@pytest.mark.parametrize(
    "grid, expected_result",
    [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
    ],
)
def test_correct_number_of_islands_is_found(grid, expected_result):
    actual_result = Solution().numIslands(grid)
    assert actual_result == expected_result
