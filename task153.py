from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] <= nums[j]: return nums[i]
            if j - i <= 1: return min(nums[i: j + 1])
            mid = (i + j) // 2
            if nums[mid] < nums[mid - 1]: return nums[mid]
            if nums[i] < nums[mid]: i = mid + 1
            else: j = mid - 1
        

s = Solution()
print(s.findMin([4,5,1,2,3]))