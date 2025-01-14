from grind75.week3.longest_common_prefix import Solution


def test_longest_common_prefix_with_shared_prefix():
    strings = ["flower", "flow", "flight"]
    expected_result = "fl"

    actual_result = Solution().longestCommonPrefix(strings)

    assert actual_result == expected_result


def test_longest_common_prefix_without_shared_prefix():
    strings = ["dog", "racecar", "car"]
    expected_result = ""

    actual_result = Solution().longestCommonPrefix(strings)

    assert actual_result == expected_result


def test_longest_common_prefix_single_input_string():
    strings = ["racecar"]
    expected_result = "racecar"

    actual_result = Solution().longestCommonPrefix(strings)

    assert actual_result == expected_result
