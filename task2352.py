"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
Example 1:
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
"""

from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:


        res = 0
        n = len(grid)
        grid_new = [[grid[i][j] for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i] == grid_new[j]: res += 1
        return res

s = Solution()
grid = [[3,2,1],[1,7,6],[2,7,7]]
print(s.equalPairs(grid))
