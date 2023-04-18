"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
Input: root = [2,1,3]
Output: true
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root: Optional[TreeNode], i, j) -> bool:
            if root is None: return True
            if not i < root.val < j: return False
            if root.left is None and root.right is None: return True
            if root.left and root.left.val >= root.val: return False
            if root.right and root.right.val <= root.val: return False
            return valid(root.left, i, root.val) and valid(root.right, root.val, j)
        return valid(root, -float('inf'), float('inf'))
        
p1 = TreeNode(5)
p2 = TreeNode(4)
p3 = TreeNode(6)
p4 = TreeNode(3)
p5 = TreeNode(7)
p1.left = p2
p1.right = p3
p3.left = p4
p3.right = p5
s = Solution()
print(s.isValidBST(p1))