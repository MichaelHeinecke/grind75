from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def apply_operator(operator: str, left_operand: int, right_operand: int) -> int:
            operations = {
                "+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y,
                "/": lambda x, y: int(x / y),
            }
            return operations[operator](left_operand, right_operand)

        stack = []
        for c in tokens:
            if c.lstrip("-").isdigit():
                stack.append(int(c))
            else:
                right_op = stack.pop()
                left_op = stack.pop()
                stack.append(apply_operator(c, left_op, right_op))

        return stack.pop()
