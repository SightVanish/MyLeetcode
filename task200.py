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
        def floodFill(image: List[List[str]], sr: int, sc: int, color: str):
            initColor = image[sr][sc]
            if color == initColor: return image
            image[sr][sc] = color
            if sr+1 < len(image) and image[sr+1][sc] == initColor: floodFill(image, sr+1, sc, color)
            if sr-1 >= 0 and image[sr-1][sc] == initColor: floodFill(image, sr-1, sc, color)
            if sc+1 < len(image[0]) and image[sr][sc+1] == initColor: floodFill(image, sr, sc+1, color)
            if sc-1 >= 0 and image[sr][sc-1] == initColor: floodFill(image, sr, sc-1, color)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    floodFill(grid, i, j, "0")
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