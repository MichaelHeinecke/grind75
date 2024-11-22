from grind75.week1.valid_palindrome import Solution


def test_valid_palindrome():
    s = "A man, a plan, a canal: Panama"

    solution = Solution()
    assert solution.isPalindrome(s) is True


def test_invalid_palindrome():
    s = "race a car"

    solution = Solution()
    assert solution.isPalindrome(s) is False


def test_string_consists_of_only_non_alphanumeric_characters():
    s = " "

    solution = Solution()
    assert solution.isPalindrome(s) is True
