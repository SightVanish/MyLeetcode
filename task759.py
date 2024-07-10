# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
class Solution:
    def employeeFreeTime(self, schedule):
        intervals = [j for i in schedule for j in i ]
        intervals.sort(key=lambda x: x[0])
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])
                del intervals[i]
            else: i += 1
        res = []
        for i in range(1, len(intervals)): res.append([intervals[i - 1][1], intervals[i][0]])
        return res

s = Solution()
print(s.employeeFreeTime(schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]))