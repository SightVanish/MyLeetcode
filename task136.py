from typing import List
# ^ stands for XOR
# 0 ^ x = x, x ^ x = 0, any sequence of x ^ y ^ z is same
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums: res ^= i
        return res