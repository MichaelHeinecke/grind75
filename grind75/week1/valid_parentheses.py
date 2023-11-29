# https://leetcode.com/problems/valid-parentheses/description/
from typing import Final, List


class Solution:
    closing_parentheses: Final[List[str]] = {")", "]", "}"}

    def is_valid(self, s: str) -> bool:
        """Checks if a string of parentheses consists of matching pairs.

        Each opening parenthesis needs to have a matching closing parenthesis.
        Nested pairs of parentheses are also valid, e.g. "({})".

        :param s: String consisting of parentheses (, ), [, ], {, }. No other
        characters are allowed.
        :return: Boolean indicating if the string s contains only matching pairs
        of parentheses.
        """
        # Optimization: If uneven number of parentheses in string, they cannot match.
        if len(s) % 2 != 0:
            return False

        opening_parentheses_stack = []
        for parenthesis in s:
            if parenthesis in self.closing_parentheses:
                # If opening parenthesis left in stack, check if it matches the
                # closing parentheses.
                if len(opening_parentheses_stack) > 0:
                    opening_parenthesis = opening_parentheses_stack.pop()
                    if not (
                        (opening_parenthesis == "(" and parenthesis == ")")
                        or (opening_parenthesis == "[" and parenthesis == "]")
                        or (opening_parenthesis == "{" and parenthesis == "}")
                    ):
                        return False
                else:  # No opening parenthesis left to match.
                    return False
            else:
                opening_parentheses_stack.append(parenthesis)

        # If opening_parentheses_stack is empty, all parentheses were matched.
        return True if len(opening_parentheses_stack) == 0 else False
