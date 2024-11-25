from grind75.week1.valid_anagram import Solution


def test_identifies_anagram():
    string_1 = "anagram"
    string_2 = "nagaram"

    solution = Solution()
    assert solution.isAnagram(string_1, string_2) is True


def test_identifies_non_anagram():
    string_1 = "car"
    string_2 = "rat"

    solution = Solution()
    assert solution.isAnagram(string_1, string_2) is False
