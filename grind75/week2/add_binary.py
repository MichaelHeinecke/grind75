class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ""

        for i in range(1, max(len(a), len(b)) + 1):
            digit_a = ord(a[-i]) - ord("0") if i <= len(a) else 0
            digit_b = ord(b[-i]) - ord("0") if i <= len(b) else 0

            total = digit_a + digit_b + carry
            res = str(total % 2) + res
            carry = total // 2

        if carry:
            res = "1" + res

        return res
