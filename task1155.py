"""
You have n dice, and each die has k faces numbered from 1 to k.
Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.
"""
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        for i in range(min(k, target)): dp[1][i+1] = 1
        def count(n, t):
            if dp[n][t] != 0: return dp[n][t]
            for i in range(k): 
                if n-1 <= t-i-1 <= k*(n-1): dp[n][t] += count(n-1, t-i-1)
            return dp[n][t]
        count(n, target)
        return dp[n][target] % mod

s = Solution()
print(s.numRollsToTarget(1, 6, 3))