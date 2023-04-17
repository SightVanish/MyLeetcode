"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""














from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[(i+j)//2] < target:
                i = (i+j)//2 + 1
            elif nums[(i+j)//2] > target:
                j = (i+j)//2 - 1
            else: 
                return (i+j)//2
        return -1