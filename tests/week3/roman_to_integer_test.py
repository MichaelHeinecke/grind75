from grind75.week2.roman_to_integer import Solution


def test_3():
    roman = "III"
    solution = Solution()
    assert solution.romanToInt(roman) == 3


def test_4():
    roman = "IV"
    solution = Solution()
    assert solution.romanToInt(roman) == 4


def test_58():
    roman = "LVIII"
    solution = Solution()
    assert solution.romanToInt(roman) == 58


def test_1994():
    roman = "MCMXCIV"
    solution = Solution()
    assert solution.romanToInt(roman) == 1994


def test_3999():
    roman = "MMMCMXCIX"
    solution = Solution()
    assert solution.romanToInt(roman) == 3999
