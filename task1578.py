"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
Return the minimum time Bob needs to make the rope colorful.
"""
from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        current_color = colors[0]
        s, m = 0, neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == current_color: m = max(m, neededTime[i])
            else:
                s += m
                m, current_color = neededTime[i], colors[i]
        return sum(neededTime) - s - m

s = Solution()
print(s.minCost(colors = "aabaa", neededTime = [1,2,3,4,1]))