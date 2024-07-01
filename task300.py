from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums == []: return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
                
s = Solution()
print(s.lengthOfLIS(nums = [1,3,6,7,9,4,10,5,6]))

