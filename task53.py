"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""
from typing import List


"""
dp = max sum of subarray of nums[:i], res = max sum of subarray of nums
if dp < 0, it means we have to start a new subarray -- we cannot retrieve the max sum of subarray with nums[i] (the subarray must be contiguous)
"""
# kadane's Algorithn
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        dp = nums[0]
        for i in range(1, len(nums)):
            dp = max(nums[i] + dp, nums[i])
            res = max(res, dp)
        return res

# DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_dp = [i for i in nums]
        for i in range(1, len(nums)):
            if max_dp[i-1] > 0: max_dp[i] += max_dp[i-1]
        return max(max_dp)
    
s = Solution()
print(s.maxSubArray([-3, -2, -3]))