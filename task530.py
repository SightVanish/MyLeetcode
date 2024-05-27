"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
Example 1:
Input: root = [4,2,6,1,3]
Output: 1
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inOrderTraversal(node: TreeNode, curr, res):
            # res: current minimum difference; curr: the value of node prior this node
            if node.left: curr, res = inOrderTraversal(node.left, curr, res)
            res = min(res, abs(node.val - curr))
            curr = node.val
            if node.right: curr, res = inOrderTraversal(node.right, curr, res)
            return curr, res
        _, res = inOrderTraversal(root, float('inf'), float('inf'))
        return int(res)


p1=TreeNode(1)
p2=TreeNode(2)
p3=TreeNode(3)
p4=TreeNode(4)
p5=TreeNode(5)
p6=TreeNode(6)
p7=TreeNode(7)
p4.left=p2
p4.right=p6
p2.left=p1
p2.right=p3
p6.left=p5
p6.right=p7

s = Solution()
print(s.getMinimumDifference(p4))