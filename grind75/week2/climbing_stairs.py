# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you
# climb to the top?


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        prev = 1
        cur = 2

        for i in range(2, n):
            prev, cur = cur, prev + cur

        return cur
