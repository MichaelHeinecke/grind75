from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = [1] * n
        postfixes = [1] * n

        for i in range(1, n):
            prefixes[i] = nums[i - 1] * prefixes[i - 1]

        for i in range(n - 2, -1, -1):
            postfixes[i] = nums[i + 1] * postfixes[i + 1]

        return [prefixes[i] * postfixes[i] for i in range(n)]
