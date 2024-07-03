from typing import List
# time: O(n^2), sapce: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))] # dp[i][j] = profit of transaction :j at ith price
        for i in range(len(prices)):
            for j in range(i):
                dp[i][0] = max(dp[i][0], dp[i - 1][0], prices[i] - prices[j])
                dp[i][1] = max(dp[i][1], dp[i - 1][1], dp[j][0] + prices[i] - prices[j]) # the second transaction must happen after the first one
        return dp[-1][1]
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices))] # dp[i][j] = profit of transaction :j at ith price
        buy_1 = prices[0]
        for i in range(len(prices)):
            if buy_1 > prices[i]: buy_1 = prices[i]
            dp[i][0] = max(dp[i - 1][0], prices[i] - buy_1)
        print(dp)


s = Solution()
print(s.maxProfit([1,2,3,4,5,1,0,10]))