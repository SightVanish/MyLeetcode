from typing import List
from heapq import heapify, heappop, heappush
from collections import defaultdict
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        ongoing_meeting = [(meetings[0][1], 0)]
        free_rooms = [i for i in range(1, n)]
        heapify(free_rooms)
        count = defaultdict(int)
        count[0] = 1
        for i in range(1, len(meetings)):
            # if we have to allocate more rooms
            if meetings[i][0] < ongoing_meeting[0][0]:
                # if free rooms, allocated one
                if free_rooms: 
                    room = heappop(free_rooms)
                    heappush(ongoing_meeting, (meetings[i][1], room))
                # if no free rooms, wait until one 
                else:
                    start_time, room = heappop(ongoing_meeting)
                    heappush(ongoing_meeting, (start_time + meetings[i][1] - meetings[i][0], room))
                count[room] += 1
            # use the first ending meeting room
            else:
                while ongoing_meeting and ongoing_meeting[0][0] <= meetings[i][0]:
                    _, room = heappop(ongoing_meeting)
                    heappush(free_rooms, room)
                room = heappop(free_rooms)
                heappush(ongoing_meeting, (meetings[i][1], room))
                count[room] += 1
        return max(count, key=count.get)
    
s = Solution()
print(s.mostBooked(n = 2, meetings = [[8,16],[17,18],[6,17],[0,13]]))

        
