from grind75.week3.palindrome_number import Solution


def test_number_is_palindrome():
    num = 121

    actual_result = Solution().isPalindrome(num)

    assert actual_result is False


def test_number_is_not_a_palindrome():
    num = 12

    actual_result = Solution().isPalindrome(num)

    assert actual_result is False


def test_negative_number_is_not_a_palindrome():
    num = -121

    actual_result = Solution().isPalindrome(num)

    assert actual_result is False
