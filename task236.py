# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is p or root is q: return root # found the target
        left_node, right_node = None, None
        if root.left: left_node = self.lowestCommonAncestor(root.left, p, q)
        if root.right: right_node = self.lowestCommonAncestor(root.right, p, q)
        # if one in left subtree and one in the right subtree, root must be the lowest common ancestor
        if left_node and right_node: return root
        # else the returned left_node or right_node itself is the lowest common ancestor
        else: return left_node or right_node
        
