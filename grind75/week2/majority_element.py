from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number_counts = defaultdict(int)
        max_count, majority_element = 0, 0

        for n in nums:
            number_counts[n] += 1
            if max_count < number_counts[n]:
                max_count = number_counts[n]
                majority_element = n

        return majority_element
