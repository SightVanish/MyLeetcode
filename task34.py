"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""
from typing import List
# the high level idea is to find target first, then expand searching based on founded target->worst case is O(n)
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
    

# find the first element of target: O(logn)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(i, j, target):
            find = False
            while i <= j:
                mid = (i + j) // 2
                if nums[mid] == target: find = True
                if nums[mid] >= target: j = mid - 1
                else: i = mid + 1
            return find, i # if find target, i is the smallest index of target; if not, i is the index of the first element > target
        find_start, start = binarySearch(0, len(nums) - 1, target)
        _, end = binarySearch(0, len(nums) - 1, target + 1)
        if not find_start: return [-1, -1]
        else: return [start, end - 1]

s = Solution()

print(s.searchRange([5,7,7,8,8,10], 7))
