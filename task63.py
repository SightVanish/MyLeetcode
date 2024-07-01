from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]: obstacleGrid[i][j] = -1
        obstacleGrid[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i - 1][0] == 1 and obstacleGrid[i][0] != -1: obstacleGrid[i][0] = 1
            else: obstacleGrid[i][0] = -1
        for j in range(1, n):
            if obstacleGrid[0][j - 1] == 1 and obstacleGrid[0][j] != -1: obstacleGrid[0][j] = 1
            else: obstacleGrid[0][j] = -1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != -1:
                    obstacleGrid[i][j] = (obstacleGrid[i - 1][j] if obstacleGrid[i - 1][j] != -1 else 0)\
                        + (obstacleGrid[i][j - 1] if obstacleGrid[i][j - 1] != -1 else 0)
        return obstacleGrid[-1][-1] if obstacleGrid[-1][-1] != -1 else 0
                
s = Solution()
print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
