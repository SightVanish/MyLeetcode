from typing import List
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
# Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j = j + 1
            i = i + 1

# Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            numbers[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in numbers and numbers[target - nums[i]] != i:
                return [i, numbers[target - nums[i]]]

# One-pass Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            if target - nums[i] in numbers:
                return [i, numbers[target - nums[i]]]
            numbers[nums[i]] = i



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i in range(0, len(nums)):
            if target - nums[i] in n:
                return [n[target - nums[i]], i]
            if nums[i] not in n:
                n[nums[i]] = i



s = Solution()
print(s.twoSum([2,7,11,15], 9))