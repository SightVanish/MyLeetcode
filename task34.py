from typing import List
class Solution:
    def findTarget(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        return start
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        start = self.findTarget(nums, target)
        print(start)
        end = self.findTarget(nums, target+1)
        
        return [start, end-1]

s = Solution()

print(s.searchRange([5,7,7,8,8,10], 6))



# find the first element >= target
def findTarget(self, nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start

# find the last element <= target
def findTarget(self, nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] <= target: # change the equality condition
            start = mid + 1 
        else:
            end = mid - 1
    return end # return end instead of start