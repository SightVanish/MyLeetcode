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
    
# modify in-place
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return intervals
        intervals.sort(key=lambda x:x[0])
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]: 
                intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])
                del intervals[i]
            else: i += 1
        return intervals

s = Solution()
print(s.merge([[2,6],[1,3],[8,10],[15,18]]))