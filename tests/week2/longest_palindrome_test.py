from grind75.week2.longest_palindrome import Solution


def test_single_character_input_is_palindrome_of_length_one():
    s = "a"
    expected_result = 1
    solution = Solution()

    actual_result = solution.longestPalindrome(s)

    assert expected_result == actual_result


def test_odd_length_input_is_odd_length_palindrome():
    s = "abccccdd"
    expected_result = 7
    solution = Solution()

    actual_result = solution.longestPalindrome(s)

    assert expected_result == actual_result


def test_even_length_input_is_even_length_palindrome():
    s = "ccccdd"
    expected_result = 6
    solution = Solution()

    actual_result = solution.longestPalindrome(s)

    assert expected_result == actual_result
