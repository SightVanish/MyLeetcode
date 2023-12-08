"""
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.
Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    res = ''
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def preorder(node: TreeNode):
            self.res += str(node.val)
            if node.left or node.right:
                self.res += '('
                if node.left: preorder(node.left)
                self.res += ')'
                if node.right:
                    self.res += '('
                    preorder(node.right)
                    self.res += ')'
        if root: preorder(root)
        return self.res   