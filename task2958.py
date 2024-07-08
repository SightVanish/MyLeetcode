from typing import List
from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        res = 0
        frequency = defaultdict(int)
        while j < len(nums):
            frequency[nums[j]] += 1
            if frequency[nums[j]] <= k: res = max(res, j - i + 1)
            else: 
                while frequency[nums[j]] > k:
                    frequency[nums[i]] -= 1
                    i += 1
            j += 1
        return res
