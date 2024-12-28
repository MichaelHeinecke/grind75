from grind75.week3.backspace_string_compare import Solution


def test_string_compare():
    s = "y#fo##f"
    t = "y#f#o##f"
    solution = Solution()
    assert solution.backspaceCompare(s, t) is True
