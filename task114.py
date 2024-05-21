# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root: 
            left, right = root.left, root.right
            if left: 
                end = left
                while end.right: end = end.right # end is the last element of left subtree
                end.right = right # connect the right subtree to the end 
                root.right = left # we only keep the right tree
                root.left = None
            root = root.right