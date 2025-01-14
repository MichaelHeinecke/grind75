from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        res = ""

        for char_index in range(len(strs[0])):
            for s in strs:
                if char_index == len(s) or s[char_index] != strs[0][char_index]:
                    return res
            res += strs[0][char_index]

        return res
