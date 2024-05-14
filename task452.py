from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0], x[1]))
        res, i = 0, 0
        while i < len(points):
            arrow = points[i][1]
            res += 1
            while i < len(points) and points[i][0] <= arrow: # consider the overlapping
                arrow = min(arrow, points[i][1])
                i += 1
        return res


s = Solution()
print(s.findMinArrowShots(points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))
