from grind75.week2.contains_duplicate import Solution


def test_single_element():
    nums = [1]
    expected_result = False
    solution = Solution()

    actual_result = solution.containsDuplicate(nums)

    assert actual_result == expected_result


def test_duplicate_present():
    nums = [1, 2, 3, 1]
    expected_result = True
    solution = Solution()

    actual_result = solution.containsDuplicate(nums)

    assert actual_result == expected_result


def test_duplicate_not_present():
    nums = [1, 2, 3, 4]
    expected_result = False
    solution = Solution()

    actual_result = solution.containsDuplicate(nums)

    assert actual_result == expected_result
