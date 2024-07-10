from typing import List
from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        history = defaultdict(int)
        for i in nums[:k]: history[i] += 1
        s = sum(nums[:k])
        res = s if len(history) == k else 0
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            history[nums[i]] += 1
            history[nums[i - k]] -= 1
            if history[nums[i - k]] == 0: del history[nums[i - k]]
            if len(history) == k: res = max(res, s)
        return res
            
s = Solution()
