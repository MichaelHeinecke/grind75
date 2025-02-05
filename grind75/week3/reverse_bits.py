class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            least_significant_bit = n & 1
            res <<= 1
            res |= least_significant_bit
            n >>= 1
        return res
