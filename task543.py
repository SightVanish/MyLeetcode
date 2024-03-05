# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def calculateDiameter(node):
            # return (height of this tree, diameter of this tree)
            if node is None: return (0, 0)
            l, r = calculateDiameter(node.left), calculateDiameter(node.right)
            # if the longest path go through current node, diameter = heigh of left subtree + height of right subtree
            return (max(l[0], r[0])+1, max(l[0]+r[0], l[1], r[1]))
        return calculateDiameter(root)[1]