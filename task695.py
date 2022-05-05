from typing import List
def printList(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end = ' ')
        print('')
class Solution:
    def findIslandDFS(self, grid, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
                return 1 + self.findIslandDFS(grid, i + 1, j) + self.findIslandDFS(grid, i - 1, j) + self.findIslandDFS(grid, i, j + 1) + self.findIslandDFS(grid, i, j - 1)
        else:
            return 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans = max(ans, self.findIslandDFS(grid, i, j))
        return ans

s = Solution()
a = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# printList(a)
print(s.maxAreaOfIsland(a))
# printList(a)