from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            mid = (i + j) // 2
            if nums[mid] == target: return mid
            if nums[mid] > target: j = mid
            if nums[mid] < target: i = mid + 1
        return i

s = Solution()
print(s.searchInsert([1,3], 0))