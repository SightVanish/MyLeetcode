from typing import List
# replace 0 with -1, task525 will be converted to task325 -- find the longest subarray with sum=0
# nums[a:b] = target -> nums[:b] - nums[:a] = target
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0: nums[i] = -1
        res = 0
        total = 0
        total_history = {0: -1} # starting point
        for i in range(len(nums)):
            total += nums[i]
            if total in total_history: res = max(res, i - total_history[total])
            else: total_history[total] = i
        return res
    
s = Solution()
print(s.findMaxLength([0, 1]))
        
        
