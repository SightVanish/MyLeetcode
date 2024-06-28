
from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                # start point=points[i]
                if points[i][0] == points[j][0]: k, b = '*', points[i][0]
                else: 
                    k = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    b = (points[j][0]*points[i][1] - points[i][0]*points[j][1]) / (points[j][0] - points[i][0])
                if (k, b) in lines:
                    if (points[j][0], points[j][1]) not in lines[(k, b)]: lines[(k, b)].add((points[j][0], points[j][1]))
                else: 
                    lines[(k, b)] = set()
                    lines[(k, b)].add((points[j][0], points[j][1]))
        res = 0
        for i in lines.values(): res = max(res, len(i))
        return res + 1

s = Solution()
print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))