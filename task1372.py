"""
You are given the root of a binary tree.
A ZigZag path for a binary tree is defined as follow:
Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
Return the longest ZigZag path contained in that tree.
"""

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node: TreeNode, left: bool, depth: int):
            if node is None: return
            self.res = max(self.res, depth)
            self.res = max(self.res, depth)
            if left: 
                if node.left: dfs(node.left, False, depth+1) # keep going
                if node.right: dfs(node.right, True, 1) # restart
            else: 
                if node.right: dfs(node.right, True, depth+1)
                if node.left: dfs(node.left, False, 1)
        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.res

p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p4 = TreeNode(4)
p5 = TreeNode(5)
p6 = TreeNode(6)
p7 = TreeNode(7)
p8 = TreeNode(8)
p1.right = p2
p2.left = p3
p2.right = p4
p4.left = p5
p4.right = p6
p5.right = p7
p7.right = p8
s = Solution()
print(s.longestZigZag(p1))