"""
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.
A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.
Note that points on the edge of a vertical area are not considered included in the area.
"""
from typing import List
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = 0
        for i in range(1, len(points)):
            res = max(res, points[i][0]-points[i-1][0])
        return res

s = Solution()
print(s.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]]))
