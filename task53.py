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

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        dp = nums[0]
        for i in range(1, len(nums)):
            dp = nums[i] + dp if dp > 0 else nums[i]
            res = max(res, dp)
        return res

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))