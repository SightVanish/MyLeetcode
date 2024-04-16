from typing import List
from heapq import heappush, heappop
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        l = list(zip(nums1, nums2))
        l.sort(key=lambda x:x[1], reverse=True)
        h = []
        res, s = 0, 0 # s = sum(h)
        for a, b in l:
            heappush(h, a) # add a to h
            s += a
            if len(h) > k: s -= heappop(h) # remove the minimum element to maintain the max sum
            if len(h) == k: res = max(res, s*b) 
        return res




s = Solution()
print(s.maxScore([1,3,3,2], [2,1,3,4], 3))