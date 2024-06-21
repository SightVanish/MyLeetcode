
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

from typing import List
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def checkLeaf(x, y, n):
            val = grid[x][y]
            for i in range(x, x + n):
                for j in range(y, y+n):
                    if grid[i][j] != val: return False
            return True
        def buildTree(x, y, n):
            if checkLeaf(x, y, n): return Node(grid[x][y], True, None, None, None, None)
            head = Node(1, False, None, None, None, None)
            head.topLeft = buildTree(x, y, n//2)
            head.topRight = buildTree(x, y+n//2, n//2)
            head.bottomLeft = buildTree(x+n//2, y, n//2)
            head.bottomRight = buildTree(x+n//2, y+n//2, n//2)
            return head
        return buildTree(0, 0, len(grid))

s = Solution()
head = s.construct(grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
print(head.topLeft.isLeaf, head.topRight.isLeaf, head.bottomLeft.isLeaf, head.bottomRight.isLeaf)