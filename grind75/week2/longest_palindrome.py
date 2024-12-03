from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = defaultdict(int)
        for char in s:
            char_count[char] += 1

        contains_odd_number = False
        count = 0
        for v in char_count.values():
            if v % 2 == 1:
                contains_odd_number = True
                count += v - 1
            else:
                count += v

        if contains_odd_number:
            count += 1

        return count
