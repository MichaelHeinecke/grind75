from grind75.week3.number_of_1_bits import Solution


def test_calculate_number_of_1_bits_1():
    integer = 11
    expected_result = 3

    actual_result = Solution().hammingWeight(integer)

    assert actual_result == expected_result


def test_calculate_number_of_1_bits_2():
    integer = 128
    expected_result = 1

    actual_result = Solution().hammingWeight(integer)

    assert actual_result == expected_result


def test_calculate_number_of_1_bits_3():
    integer = 2147483645
    expected_result = 30

    actual_result = Solution().hammingWeight(integer)

    assert actual_result == expected_result
