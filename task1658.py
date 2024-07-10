from typing import List
# this task can be converted to: find the longest subarry whose sum=totalsum - x -> sliding window
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if not nums:
            if x: return -1
            else: return 0
        target = sum(nums) - x
        if target == 0: return len(nums)
        i, j = 0, 0
        current_sum = nums[0]
        res = -1
        while i < len(nums):
            while current_sum < target and j < len(nums):
                j += 1
                if j < len(nums): current_sum += nums[j]
            if current_sum == target: res = max(res, j - i + 1)   
            current_sum -= nums[i]           
            i += 1
            
        return len(nums) - res if res != -1 else -1

s = Solution()
print(s.minOperations([5], 5))