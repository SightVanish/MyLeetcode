# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_value = -float('inf')
        def maxSubtree(root):
            # the max value of the path including root
            nonlocal max_value
            if root is None: return 0
            left_value, right_value = max(maxSubtree(root.left), 0), max(maxSubtree(root.right), 0) # do not add this node if maxSubtree < 0
            max_value = max(max_value, left_value + root.val + right_value) # this max_value will consider all subtrees
            return root.val + max(left_value, right_value) # for the return value, root is not taken as the root of the subtree->so we have to choose a path either left or right
        maxSubtree(root)
        return max_value
