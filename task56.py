from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return []
        intervals.sort(key=lambda x:x[0])
        res = []
        start, end = intervals[0][0], intervals[0][1]
        for i, j in intervals:
            if i > end:
                res.append([start, end])
                start, end = i, j
            else:
                end = max(end, j)
        res.append([start, end])
        return res

s = Solution()
print(s.merge([[2,6],[1,3],[8,10],[15,18]]))