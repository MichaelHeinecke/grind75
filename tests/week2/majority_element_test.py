from grind75.week2.majority_element import Solution


def test_majority_element_1():
    nums = [3, 2, 3]
    expected_result = 3
    solution = Solution()

    actual_result = solution.majorityElement(nums)

    assert expected_result == actual_result


def test_majority_element_2():
    nums = [2, 2, 1, 1, 1, 2, 2]
    expected_result = 2
    solution = Solution()

    actual_result = solution.majorityElement(nums)

    assert expected_result == actual_result
