"""
Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.
Note:
The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
A subtree of root is a tree consisting of root and all of its descendants.
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def check_avg(root):
            nonlocal res
            if root is None: return 0, 0
            left_sum, left_n = check_avg(root.left)
            right_sum, right_n = check_avg(root.right)
            sum, n = left_sum + right_sum + root.val, left_n + right_n + 1
            if root.val == sum // n: res += 1
            return sum, n
        check_avg(root)
        return res
        

s = Solution()
print(s.averageOfSubtree(None))

        