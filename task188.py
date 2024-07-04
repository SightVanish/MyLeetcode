# check task123 before this one
from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0
        min_prices = [prices[0]] * k
        profit = [0] * k
        for i in range(1, len(prices)):
            for j in range(k):
                if j == 0: min_prices[j] = min(min_prices[j], prices[i])
                else: min_prices[j] = min(min_prices[j], prices[i] - profit[j - 1])
                profit[j] = max(profit[j], prices[i] - min_prices[j])
        return profit[-1]
