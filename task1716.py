"""
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
"""

class Solution:
    def totalMoney(self, n: int) -> int:
        k = n // 7
        return (28+21+k*7)*k//2 + (k+1+k+n-7*k)*(n-7*k)//2

s = Solution()
print(s.totalMoney(20))