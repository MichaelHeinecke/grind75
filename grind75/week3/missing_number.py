from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)

        for i in range(len(nums) + 1):
            if i not in nums_set:
                return i

    def missingNumberConstantSpace(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums) + 1):
            s += i

        for num in nums:
            s -= num

        return s
