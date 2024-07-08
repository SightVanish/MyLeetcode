# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            # return is_balanced, height of tree
            if root is None: return True, 0
            left_tree, left_hight = height(root.left)
            right_tree, right_height = height(root.right)
            return left_tree and right_tree and abs(left_hight - right_height) <= 1, max(left_hight, right_height) + 1
        balanced, _ = height(root)
        return balanced

        
