# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrderTravesal(root, index):
            res = 0
            if index < k and root.left: res, index = inOrderTravesal(root.left, index)
            index += 1
            if index == k: return root.val, index
            if index < k and root.right: res, index = inOrderTravesal(root.right, index)
            return res, index
        res, _ = inOrderTravesal(root, 0)
        return res

p1 = TreeNode(1)
p2 = TreeNode(2)
p3 = TreeNode(3)
p4 = TreeNode(4)
p5 = TreeNode(5)
p5.left = p3
p3.left = p2
p3.right = p4
p2.left = p1
s = Solution()
print(s.kthSmallest(p5, 3))
