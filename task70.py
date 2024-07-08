class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n)]
        def climb(n):
            if n <= 2: dp[n] = n + 1
            elif dp[n] == -1: dp[n] = climb(n - 1) + climb(n - 2)
            return dp[n]
        climb(n-1)
        return dp[-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        dp = [1, 2]
        for i in range(2, n): dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]

# O(1) space complexity
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        step1, step2 = 1, 2
        for _ in range(2, n): step1, step2 = step2, step1 + step2
        return step2  

s = Solution()
print(s.climbStairs(2))