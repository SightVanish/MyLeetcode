# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res, curr, next = [], [root], []
        while curr:
            values = [i.val for i in curr]
            res.append(sum(values)/len(values))
            for i in curr:
                if i.left: next.append(i.left)
                if i.right: next.append(i.right)
            curr, next = next, []
        return res
