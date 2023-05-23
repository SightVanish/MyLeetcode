"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
"""
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        res = 0
        x = abs(x)
        while x:
            res = res * 10 + x % 10
            x //= 10
        res *= sign
        if res > 2**31 - 1 or res < -2**31: return 0
        else: return res


s = Solution()
print(s.reverse(1534236469))


