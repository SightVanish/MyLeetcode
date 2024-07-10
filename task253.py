from typing import List
from heapq import heapify, heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x:x[0])
        ongoing_meeting = [intervals[0][1]]
        count = 1
        for i in range(1, len(intervals)):
            start_time = intervals[i][0]
            while ongoing_meeting and ongoing_meeting[0] <= start_time: heappop(ongoing_meeting)
            heappush(ongoing_meeting, intervals[i][1])
            count = max(count, len(ongoing_meeting))
        return count

s = Solution()
print(s.minMeetingRooms([[2,5],[1,10],[3,7],[8,11],[13,15],[4,16]]))



