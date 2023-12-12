"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""

from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i = max(nums)
        j = nums.index(i)
        return (max(nums[0:j] + nums[j+1:])-1) * (i-1)