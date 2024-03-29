"""
You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.
You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.
There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.
Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.
Return the minimum number of minutes needed to pick up all the garbage.
"""

from typing import List
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        dist = [0, 0, 0]
        for i in range(len(garbage)):
            if 'M' in garbage[i]:
                res += dist[0] + garbage[i].count('M')
                dist[0] = 0
            if 'P' in garbage[i]:
                res += dist[1] + garbage[i].count('P')
                dist[1] = 0
            if 'G' in garbage[i]:
                res += dist[2] + garbage[i].count('G')
                dist[2] = 0
            if i < len(travel): 
                dist[0] += travel[i]
                dist[1] += travel[i]
                dist[2] += travel[i]
        return res

s = Solution()
print(s.garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10]))
