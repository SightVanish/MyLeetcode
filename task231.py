"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        while n > 1:
            n /= 2
            if int(n) != n: return False
        return True
s = Solution()
print(s.isPowerOfTwo(-8))