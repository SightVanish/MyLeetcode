"""
Given an m x n 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res, m, n = 0, len(grid), len(grid[0])
        def expandLand(i, j):
            # based on grid[i][j], find all adjacent lands and turn to -1
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                grid[i][j] = '0'
                if i > 0 and grid[i - 1][j] == '1': stack.append([i - 1, j])
                if i < m - 1 and grid[i + 1][j] == '1': stack.append([i + 1, j])
                if j > 0 and grid[i][j - 1] == '1': stack.append([i, j - 1])
                if j < n - 1 and grid[i][j + 1] == '1': stack.append([i, j + 1])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': 
                    expandLand(i, j)
                    res += 1
        return res
    
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

s = Solution()
print(s.numIslands(grid))