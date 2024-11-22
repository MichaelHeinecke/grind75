from grind75.week1.best_time_to_buy_and_sell_stock import Solution


def test_highest_profit_is_found():
    prices = [7, 1, 5, 3, 6, 4]
    max_profit = 5

    solution = Solution()
    assert solution.maxProfit(prices) == max_profit


def test_if_no_profit_can_be_made_profit_is_zero():
    prices = [7, 6, 4, 3, 1]
    max_profit = 0

    solution = Solution()
    assert solution.maxProfit(prices) == max_profit
