from typing import List
# same as task525
class Solution:
    def maxSubArrayLen(self, nums: List[int], target: int) -> int:
        res = 0
        total = 0
        total_history = {0: -1} # starting point
        for i in range(len(nums)):
            total += nums[i]
            if total - target in total_history: res = max(res, i - total_history[total - target])
            elif total not in total_history: total_history[total] = i # only keep the smallest index with sum=total
        return res

s = Solution()
print(s.maxSubArrayLen([1, -1, 5, -2, 3], 3))