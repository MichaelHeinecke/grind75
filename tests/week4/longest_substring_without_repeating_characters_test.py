import pytest

from grind75.week4.longest_substring_without_repeating_characters import Solution


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("pwwkewabcdp", 8),
    ],
)
def test_binary_tree_level_order_traversal(string, expected_result):
    actual_result = Solution().lengthOfLongestSubstring(string)
    assert actual_result == expected_result
