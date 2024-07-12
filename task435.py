from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        end = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if end > intervals[i][0]:
                res += 1
                end = min(end, intervals[i][1])
            else: end = intervals[i][1]
        return res

s = Solution()
print(s.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]))
