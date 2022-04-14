from typing import List
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        ans = str(nums[0])
        ans += '/('
        for n in nums[1:]:
            ans += str(n)
            ans += '/'
        return ans[:-1] + ')'