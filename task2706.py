"""
You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.
You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.
Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.
"""
from typing import List
# quick selecion
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # this is a top-k problem
        def partition(l, r):
            pivot = prices[l]
            while l < r:
                while prices[r] >= pivot and r > l: r -= 1
                prices[l] = prices[r]
                while prices[l] <= pivot and r > l: l += 1
                prices[r] = prices[l]
            prices[l] = pivot
            return l
        def selection(l , r):
            if l >= r: return
            pivot = partition(l, r)
            if pivot == 2: return
            elif pivot > 2: selection(l, pivot - 1)
            elif pivot < 2: selection(pivot + 1, r)
        selection(0, len(prices) - 1)
        if sum(prices[:2]) <= money: return money - sum(prices[:2])
        else: return money

# use heap
import heapq
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        heapq.heapify(prices)
        m = heapq.heappop(prices)
        n = heapq.heappop(prices)
        if m + n <= money: return money - m - n
        else: return money

# go through prices once
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # p1 stands for the minimum, p2 stands for the second minimum
        p1, p2 = float('inf'), float('inf')
        for p in prices:
            if p < p1:
                p1, p2 = p, p1
            elif p < p2:
                p2 = p
        if p1 + p2 <= money: return money - p1 - p2
        else: return money

s = Solution()
print(s.buyChoco([2,1,0], 1))