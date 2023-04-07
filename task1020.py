from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def DFS(i, j):
            grid[i][j] = 0
            for (x, y) in (i, j-1), (i, j+1), (i-1, j), (i+1, j):
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    grid[x][y] = 0
                    DFS(x, y)

        for i in range(m):
            if grid[i][0]: DFS(i, 0)
            if grid[i][n-1]: DFS(i, n-1)
        for j in range(n):
            if grid[0][j]: DFS(0, j)
            if grid[m-1][j]: DFS(m-1, j)

        return sum(sum(row) for row in grid)
    
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
s = Solution()
print(s.numEnclaves(grid))