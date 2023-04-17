"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return None
        res = []
        l = [root]
        while l:
            res.append(l)
            l = []
            for i in res[-1]:
                if i.left: l.append(i.left)
                if i.right: l.append(i.right)
        return [[i.val for i in l] for l in res]






