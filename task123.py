from typing import List
# time: O(n^2), sapce: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [[0, 0] for _ in range(len(prices))] # dp[i][j] = profit of transaction :j at ith price
        for i in range(len(prices)):
            for j in range(i):
                dp[i][0] = max(dp[i][0], dp[i - 1][0], prices[i] - prices[j])
                dp[i][1] = max(dp[i][1], dp[i - 1][1], dp[j][0] + prices[i] - prices[j]) # the second transaction must happen after the first one
        return dp[-1][1]

# time: O(n), sapce: O(n) 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        dp = [[0, 0] for _ in range(len(prices))] # dp[i][j] = profit of transaction :j at ith price
        # -> first transaction
        min_price = prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            dp[i][0] = max(dp[i - 1][0], prices[i] - min_price)
        # <- second transaction
        max_price = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            max_price = max(max_price, prices[i])
            dp[i][1] = max(dp[i+1][1], max_price - prices[i])
        # total
        res = 0
        for i in range(len(prices)): res = max(res, dp[i][0] + dp[i][1])
        return res
    
# time: O(n), sapce: O(1) 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        min_price_1 = prices[0]
        min_price_2 = prices[0]
        profit_1 = 0
        profit_2 = 0
        for i in range(1, len(prices)):
            min_price_1 = min(min_price_1, prices[i])
            profit_1 = max(profit_1, prices[i] - min_price_1)
            min_price_2 = min(min_price_2, prices[i] - profit_1) # price at day 1 is $10 but we already have $5 so the real price is $10-$5
            profit_2 = max(profit_2, prices[i] - min_price_2)
        return profit_2

s = Solution()
print(s.maxProfit([1,2,3,4,5,1,0,10]))