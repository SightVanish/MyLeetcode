"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""
from typing import List
# the high level idea is to find target first, then expand searching based on founded target
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right, mid = 0, len(nums) - 1, 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: 
                left, right = mid, mid
                while left >= 0 and nums[left] == nums[mid]: left -= 1
                while right < len(nums) and nums[right] ==  nums[mid]: right += 1
                return [left+1, right-1]
            elif nums[mid] > target: right = mid - 1
            else: left = mid + 1
        return [-1, -1]
    

class Solution:
    def findTarget(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        return start # start makes sure it always be the first element == target
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums: return [-1, -1] # handle corner cases
        start = self.findTarget(nums, target)
        end = self.findTarget(nums, target+1) # find the first element bigger than target
        return [start, end-1]

s = Solution()

print(s.searchRange([5,7,7,8,8,10], 7))
