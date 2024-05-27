# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        reverse, res, curr, next = False, [], [root], []
        while curr:
            values = [i.val for i in curr]
            res.append(values[::-1] if reverse else values)
            reverse = False if reverse else True
            for i in curr:
                if i.left: next.append(i.left)
                if i.right: next.append(i.right)
            curr, next = next, []
        return res
