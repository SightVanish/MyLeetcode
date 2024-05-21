# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        length = len(inorder)
        inorder_index = {inorder[i]: i for i in range(length)}
        def buildSubTree(post_start, post_end, in_start, in_end):
            # find root
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            # spilt tree to left and right
            inorder_root_index = inorder_index[root_val]
            left_subtree_length = inorder_root_index - in_start
            # build left tree
            if inorder_root_index > in_start: root.left = buildSubTree(post_start, post_start + left_subtree_length - 1, in_start, inorder_root_index - 1)
            # build right tree
            if inorder_root_index < in_end: root.right = buildSubTree(post_start + left_subtree_length, post_end - 1, inorder_root_index + 1, in_end)
            return root
        return buildSubTree(0, length - 1, 0, length - 1)
