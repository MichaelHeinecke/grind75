from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars_in_magazine = Counter(magazine)

        for char in ransomNote:
            if char in chars_in_magazine and chars_in_magazine[char] >= 1:
                chars_in_magazine[char] -= 1
            else:
                return False

        return True
