from grind75.week3.missing_number import Solution


def test_missing_number_is_found_1():
    nums = [3, 0, 1]
    expected_result = 2

    actual_result = Solution().missingNumber(nums)

    assert actual_result == expected_result


def test_missing_number_is_found_2():
    nums = [0, 1]
    expected_result = 2

    actual_result = Solution().missingNumber(nums)

    assert actual_result == expected_result


def test_missing_number_is_found_3():
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    expected_result = 8

    actual_result = Solution().missingNumber(nums)

    assert actual_result == expected_result


def test_constant_space_missing_number_is_found_1():
    nums = [3, 0, 1]
    expected_result = 2

    actual_result = Solution().missingNumberConstantSpace(nums)

    assert actual_result == expected_result


def test_constant_space_missing_number_is_found_2():
    nums = [0, 1]
    expected_result = 2

    actual_result = Solution().missingNumberConstantSpace(nums)

    assert actual_result == expected_result


def test_constant_space_missing_number_is_found_3():
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    expected_result = 8

    actual_result = Solution().missingNumberConstantSpace(nums)

    assert actual_result == expected_result
