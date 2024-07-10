from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, res = 0, []
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        res.append(newInterval)
        while i < len(intervals) and intervals[i][0] > newInterval[1]:
            res.append(intervals[i])
            i += 1
        return res
 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def findStart(i, j):
            while i <= j:
                if intervals[j][0] < newInterval[0]: return j + 1
                if intervals[i][0] > newInterval[0]: return i
                mid = (i + j) // 2
                if intervals[mid][0] == newInterval[0]: return mid
                if intervals[mid][0] < newInterval[0]: i = mid + 1
                else: j = mid - 1
        if not intervals: return [newInterval]
        start = findStart(0, len(intervals) - 1)
        if start == len(intervals):
            if newInterval[0] <= intervals[-1][1]: intervals[-1][1] = max(intervals[-1][1], newInterval[1])
            else:intervals.append(newInterval)
            return intervals
        while len(intervals) > start and newInterval[1] >= intervals[start][0]: 
            newInterval[1] = max(newInterval[1], intervals[start][1])
            del intervals[start]     
        if start == 0: intervals = [newInterval] + intervals
        else: 
            if intervals[start - 1][1] >= newInterval[0]: intervals[start - 1][1] = max(intervals[start - 1][1], newInterval[1])
            else: intervals = intervals[:start] + [newInterval] + intervals[start:]
        return intervals
        
s = Solution()
print(s.insert([[0,5],[9,12]], [7,16]))
