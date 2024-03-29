"""
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.
If the tree has more than one mode, return them in any order.
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
"""


from typing import Optional, List
from collections import Counter
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        elements = [] # sort elements via in-order traversal
        def inorder(root):
            if root is None: return 
            elements.append(root.val)
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        count = Counter(elements)
        m = max(count.values()) # this would be a little bit faster
        return [i for i in count if count[i]==m]
        



        
