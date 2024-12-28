from grind75.week3.counting_bits import Solution


def test_counting_bits_0():
    i = 0
    solution = Solution()
    expected_result = [0]

    actual_result = solution.countBits(i)

    assert actual_result == expected_result


def test_counting_bits_2():
    i = 2
    solution = Solution()
    expected_result = [0, 1, 1]

    actual_result = solution.countBits(i)

    assert actual_result == expected_result


def test_counting_bits_5():
    i = 5
    solution = Solution()
    expected_result = [0, 1, 1, 2, 1, 2]

    actual_result = solution.countBits(i)

    assert actual_result == expected_result
