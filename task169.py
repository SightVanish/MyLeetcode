"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i in count: count[i] += 1
            else: count[i] = 1
            if count[i] >= len(nums) / 2: return i
    

# Moore Voting Algorithm -- based on the assumption that the majority number will always gain the lead in the end
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, candidate = 0, 0
        for i in nums:
            if count == 0: 
                candidate = i
                count += 1
            elif i == candidate: count += 1
            else: count -= 1
        return candidate