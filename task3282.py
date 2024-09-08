from typing import List
# O(n^2) time complexity
class Solution1:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(1, n):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] + (i - j) * nums[j])
        return dp[-1]

# it can be proven the best strategy is to always pick the nearest index with larger number
# suppost we are at a (with value m), the next index with larger number is b (with value n > m), the target is c
# a -> c: score = (c-a)*m = (b-a)*m + (c-b)*m
# a -> b -> c: score = (b-a)*m + (c-b)*n
# a -> b -> c always greater than a -> c
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        score = 0
        index = 0
        # always pick the nearest index with larger number
        for i in range(1, len(nums)):
            if nums[i] > nums[index]:
                score += (i - index) * nums[index]
                index = i
        # last jump
        score += (len(nums) - 1 - index) * nums[index]
        return score
        
