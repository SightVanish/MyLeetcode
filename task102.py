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
        if root is None: return []
        res, curr, next = [], [root], []
        while curr:
            res.append([i.val for i in curr])
            for i in curr:
                if i.left: next.append(i.left)
                if i.right: next.append(i.right)
            curr, next = next, []
        return res
