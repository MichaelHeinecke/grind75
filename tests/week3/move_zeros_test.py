from grind75.week3.move_zeros import Solution


def test_order_of_non_zero_elements_is_maintained():
    nums = [0, 1, 0, 3, 12]
    expected_result = [1, 3, 12, 0, 0]

    Solution().moveZeroes(nums)

    assert nums == expected_result


def test_single_zero_list_is_unchanged():
    nums = [0]
    expected_result = [0]

    Solution().moveZeroes(nums)

    assert nums == expected_result


def test_multiple_subsequent_zeros_are_moved_to_end_of_list():
    nums = [0, 0, 1]
    expected_result = [1, 0, 0]

    Solution().moveZeroes(nums)

    assert nums == expected_result
