from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [-1 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            if i in coins: dp[i] = 1
            else: 
                remains = []
                for c in coins:
                    if i - c > 0 and dp[i - c] != -1: remains.append(dp[i - c])
                if remains: dp[i] = min(remains) + 1
        return dp[-1]

s = Solution()
print(s.coinChange(coins = [2], amount = 3))
