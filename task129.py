# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        def path(root, value):
            if root.left is None and root.right is None: return int(value + str(root.val))
            return (path(root.left, value + str(root.val)) if root.left else 0) + (path(root.right, value + str(root.val)) if root.right else 0)
        return path(root, '')
