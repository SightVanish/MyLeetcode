from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]
        def robMoney(i):
            if i == 0: dp[i] = nums[i]
            elif i == 1: dp[i] = max(nums[:2])
            elif dp[i] == -1: dp[i] = max(robMoney(i - 1), robMoney(i - 2) + nums[i])
            return dp[i]
        robMoney(len(nums) - 1)
        return dp[-1]
    
s = Solution()
print(s.rob([1,2,3,1]))