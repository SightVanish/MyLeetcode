from typing import List
# split nums to two part
# it is easy to check whether target is in an ordered part but hard to check whether target is in an unordered part. so we avoid checking target in the unordered part.
# if left part is in order, we check whether target is in this one or not.
# if left part is not in order, then the right part must be in order, so we can check whether target is in right part or not.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]: # note: '=' should be included here.
                # the left part is in order
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

s = Solution()
print(s.search([3,1], 1))