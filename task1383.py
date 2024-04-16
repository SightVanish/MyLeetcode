# generally same as task2542
from typing import List
from heapq import heappush, heappop
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        l = list(zip(speed, efficiency))
        l.sort(key=lambda x:x[1], reverse=True)
        res, s = 0, 0
        h = []
        for a, b in l:
            heappush(h, a)
            s += a
            if len(h) > k: s -= heappop(h)
            res = max(res, s*b)
        return res % (10**9+7)