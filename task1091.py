"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2
"""

from typing import List
class Solution:
    # BFS and record the lenght
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: return -1
        if len(grid) == 1 and len(grid[0]) == 1: return 1
        bfs = [(0,0,1)]
        while bfs:
            i, j, depth = bfs[0]
            bfs = bfs[1:]
            # for adjacent nodes
            for m, n in ((i-1, j-1), (i, j-1), (i+1, j-1), (i-1, j), (i+1, j), (i-1, j+1), (i, j+1), (i+1, j+1)):
                if m in range(len(grid)) and n in range(len(grid[0])) and grid[m][n] == 0:
                    if m == len(grid) - 1 and n == len(grid[0]) - 1: return depth + 1
                    bfs.append((m, n, depth+1))
                    grid[m][n] = 1

        return -1


s = Solution()
print(s.shortestPathBinaryMatrix([[0]]))


