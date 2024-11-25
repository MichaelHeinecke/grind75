from grind75.week1.binary_search import Solution


def test_search_target_exists():
    numbers = [-1, 0, 3, 5, 9, 12]
    target = 9
    expected_output = 4

    solution = Solution()
    assert solution.search(numbers, target) == expected_output


def test_search_target_does_not_exists():
    numbers = [-1, 0, 3, 5, 9, 12]
    target = 2
    expected_output = -1

    solution = Solution()
    assert solution.search(numbers, target) == expected_output


def test_empty_list():
    numbers = []
    target = 4
    expected_output = -1

    solution = Solution()
    assert solution.search(numbers, target) == expected_output
