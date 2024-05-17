"""
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        layers, pre, next = 0, [root], []
        while pre:
            for i in pre: 
                if i.left: next.append(i.left)
                if i.right: next.append(i.right)
            pre, next = next, []
            layers += 1
        return layers        