class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res = 0
        i = 0

        while i < len(s):
            current = roman_to_int_map[s[i]]
            if i < len(s) - 1:
                following = roman_to_int_map[s[i + 1]]
                if following > current:
                    current = following - current
                    i += 1
            res += current
            i += 1

        return res
