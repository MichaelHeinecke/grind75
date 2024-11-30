from grind75.week1.first_bad_version import Solution


def test_first_bad_version_at_four():
    n = 5
    expected_result = 4
    solution = Solution()

    actual_result = solution.firstBadVersion(n)

    assert actual_result == expected_result
