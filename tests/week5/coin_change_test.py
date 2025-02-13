import pytest

from grind75.week5.coin_change import Solution


@pytest.mark.parametrize(
    "coins, amount, expected_result",
    [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ],
)
def test_least_number_of_coins_is_found(coins, amount, expected_result):
    actual_result = Solution().coinChange(coins, amount)
    assert actual_result == expected_result
