from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j, res, total = 0, 0, len(nums)+1, 0
        while j < len(nums):
            while total < target and j < len(nums):
                total += nums[j]
                j += 1
            while total >= target and i <= j:
                res = min(res, j - i)
                total -= nums[i]
                i += 1
        return 0 if res > len(nums) else res
        
s = Solution()
print(s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))