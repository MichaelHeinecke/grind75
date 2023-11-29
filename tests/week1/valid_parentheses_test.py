import pytest

from grind75.week1.valid_parentheses import Solution


@pytest.fixture
def solution():
    return Solution()


def test_pair_of_matching_parentheses_is_valid(solution):
    input_string = "()"
    output = solution.is_valid(input_string)
    assert output is True


def test_three_pairs_of_matching_parentheses_are_valid(solution):
    input_string = "()[]{}"
    output = solution.is_valid(input_string)
    assert output is True


def test_nested_matching_pairs_of_parentheses_are_valid(solution):
    input_string = "([]{})"
    output = solution.is_valid(input_string)
    assert output is True


def test_nested_non_matching_pairs_of_parentheses_are_invalid(solution):
    input_string = "([]{])"
    output = solution.is_valid(input_string)
    assert output is False


def test_pair_of_non_matching_parentheses_is_invalid(solution):
    input_string = "(}"
    output = solution.is_valid(input_string)
    assert output is False


def test_single_opening_parenthesis_is_invalid(solution):
    input_string = "("
    output = solution.is_valid(input_string)
    assert output is False


def test_single_closing_parenthesis_is_invalid(solution):
    input_string = "]"
    output = solution.is_valid(input_string)
    assert output is False
