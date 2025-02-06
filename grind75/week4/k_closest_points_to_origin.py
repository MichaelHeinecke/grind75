import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda e: math.sqrt(pow(0 - e[0], 2) + pow(0 - e[1], 2)))
        return points[:k]
