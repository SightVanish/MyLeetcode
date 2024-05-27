# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def height(self, root, left=False):
        height = 0
        while root:
            height += 1
            if left: root = root.left
            else: root = root.right
        return height
            
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        left_subtree_height = self.height(root.left, True)
        right_subtree_height = self.height(root.right, False) # right subtree height is not technically the height but the minimum hight
        # if the subtree heights are same, it means this is a perfect binary tree
        if left_subtree_height == right_subtree_height: return 2 ** (left_subtree_height + 1) - 1
        else: return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# O(log(n)) recursions and in each steps O(log(n)) to find height -- O((log(n))^2)