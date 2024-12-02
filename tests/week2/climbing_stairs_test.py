from grind75.week2.climbing_stairs import Solution


def test_two_stairs_have_two_possible_ways():
    number_of_stairs = 2
    expected_result = 2
    solution = Solution()

    actual_result = solution.climbStairs(number_of_stairs)

    assert expected_result == actual_result


def test_three_stairs_have_three_possible_ways():
    number_of_stairs = 3
    expected_result = 3
    solution = Solution()

    actual_result = solution.climbStairs(number_of_stairs)

    assert expected_result == actual_result
