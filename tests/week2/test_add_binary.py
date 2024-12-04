from grind75.week2.add_binary import Solution


def test_add_0_and_0():
    a = "0"
    b = "0"
    expected_result = "0"
    solution = Solution()

    actual_result = solution.addBinary(a, b)

    assert actual_result == expected_result


def test_add_1_and_0():
    a = "0"
    b = "1"
    expected_result = "1"
    solution = Solution()

    actual_result = solution.addBinary(a, b)

    assert actual_result == expected_result


def test_add_numbers_with_different_length_digits():
    a = "11"
    b = "1"
    expected_result = "100"
    solution = Solution()

    actual_result = solution.addBinary(a, b)

    assert actual_result == expected_result


def test_add_numbers_with_same_length_digits():
    a = "1010"
    b = "1011"
    expected_result = "10101"
    solution = Solution()

    actual_result = solution.addBinary(a, b)

    assert actual_result == expected_result
