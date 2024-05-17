# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        pre, curr = [root], []
        while pre:
            for i in pre: 
                if i is not None: curr += [i.left, i.right]
            for i in range(len(curr) // 2):
                if (curr[i] is None or curr[-(i+1)] is None) and curr[i] != curr[-(i+1)]: return False
                if curr[i] is not None and curr[i].val != curr[-(i+1)].val: return False
            pre, curr = curr, []
        return True
