# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        length = len(preorder)
        inorder_index = {inorder[i]: i for i in range(length)}        
        def buildSubTree(pre_start, pre_end, in_start, in_end):
            # find the root value of current subtree
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            # split the subtree to left and right
            inorder_root_index = inorder_index[root_val]
            left_subtree_length = inorder_root_index - in_start
            # build the left subtree
            if inorder_root_index > in_start: root.left = buildSubTree(pre_start + 1, pre_start + left_subtree_length, in_start, inorder_root_index - 1)
            if inorder_root_index < in_end: root.right = buildSubTree(pre_start + left_subtree_length + 1, pre_end, inorder_root_index + 1, in_end)
            return root
        return buildSubTree(0, length - 1, 0, length - 1)

        
s = Solution()
s.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])