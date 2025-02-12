import pytest

from grind75.week5.evaluate_reverse_polish_notation import Solution


@pytest.mark.parametrize(
    "tokens, expected_result",
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ],
)
def test_notation_is_evaluated_correctly(tokens, expected_result):
    actual_result = Solution().evalRPN(tokens)
    assert actual_result == expected_result
