from grind75.week3.single_number import Solution


def test_single_number_is_found_in_multiple_element_array():
    nums = [4, 1, 2, 1, 2]
    expected_result = 4

    actual_result = Solution().singleNumber(nums)

    assert actual_result == expected_result


def test_single_number_is_found_in_single_element_array():
    nums = [1]
    expected_result = 1

    actual_result = Solution().singleNumber(nums)

    assert actual_result == expected_result
