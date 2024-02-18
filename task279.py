"""
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
"""
import math

class Solution:
    def numSquares(self, n: int) -> int:
        l = [-1 for _ in range(n+1)]
        for i in range(1, int(math.sqrt(n))+1): l[i*i] = 1
        def findOptimal(m):
            if l[m] != -1: return l[m]
            tmp = [findOptimal(m-i*i) for i in range(1, int(math.sqrt(m))+1)]
            l[m] = min(tmp) + 1
            return l[m]
        res = findOptimal(n)
        return res
    
# same idea, but optimized in space
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            val = float('inf')
            j = 1
            while j*j <= i:
                val = min(val, dp[i-j*j]+1)
                j += 1
            dp[i] = val
        return dp[-1]


s = Solution()
print(s.numSquares(12))
