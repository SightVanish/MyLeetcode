"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""
from typing import List
# the high level idea is to find the pivot first, then find target in a sorted list
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while right > left + 1:
            mid = (right + left) // 2
            if nums[mid] > nums[left]: left = mid
            else: right = mid

        if nums[right] <= target <= nums[-1]: left, right = right, len(nums) - 1
        elif nums[0] <= target <= nums[left]: left, right = 0, left
        else: return -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            elif nums[mid] <= target: left = mid + 1
            else: right = mid - 1
        return -1
        

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] < nums[mid]:
                # nums[start: mid+1] is sorted
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # nums[mid: -1] is sorted
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

s = Solution()
print(s.search([3,1], 1))