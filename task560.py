from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        history = defaultdict(int)
        history[0] = 1
        s = 0
        res = 0
        for i in range(len(nums)):
            s += nums[i]
            res += history[s - k]
            history[s] += 1
        return res
