"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i, j = 0, 0
        while j < len(prices):
            if prices[i] > prices[j]: # the key is that we always make the prices[i] minimum
                i = j
            else:
                profit = prices[j] - prices[i]
                if profit > res:
                    res = profit
            j += 1
        return res

s = Solution()
print(s.maxProfit([7,6,5,4,3,2,1]))

