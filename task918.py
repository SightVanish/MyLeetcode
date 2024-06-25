from typing import List
# kadane's Algorithn
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) < 0: return max(nums) # have to add this line as we cannot return an empty subarray
        max_dp = max_res = min_dp = min_res = nums[0]
        for i in range(1, len(nums)):
            max_dp = max(max_dp + nums[i], nums[i])
            min_dp = min(min_dp + nums[i], nums[i])
            max_res = max(max_res, max_dp)
            min_res = min(min_res, min_dp)
        return max(max_res, sum(nums) - min_res)

s = Solution()
print(s.maxSubarraySumCircular(nums = [2, -2]))
