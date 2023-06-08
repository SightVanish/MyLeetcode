"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
"""

from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        i = 0
        while i < len(grid):
            if grid[i][-1] < 0: break
            i += 1
        j = len(grid[0]) - 1
        while j >= 0 and i < len(grid):
            if grid[i][j] < 0: j -= 1
            else:
                res += len(grid[0]) - j - 1
                i += 1
        if j == -1 and i < len(grid): res += (len(grid) - i) * len(grid[0])
        return res

s = Solution()
grid = [[1,-1],[-1,-1]]
print(s.countNegatives(grid))
