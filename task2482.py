"""
You are given a 0-indexed m x n binary matrix grid.
A 0-indexed m x n difference matrix diff is created with the following procedure:
Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.
"""
from typing import List
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        r = [sum(i) for i in grid]
        c = [sum([grid[i][j] for i in range(m)]) for j in range(n)]
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2*(r[i]+c[j]) - (m+n)
        return grid


s = Solution()
print(s.onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))