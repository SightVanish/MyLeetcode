# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
# O(n) for space and time
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        curr, next, res = [root], [], []
        while curr:
            res.append(curr[-1].val)
            for i in curr:
                if i.left: next.append(i.left)
                if i.right: next.append(i.right)
            curr, next = next, []
        return res

# O(1) in space and O(n) in time  
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def count(root, level):
            if root is None: return 
            if len(res) == level: res.append(root.val) # if the rightmost element at this level has not been found, add this one
            count(root.right, level + 1) # check the right subtree first
            count(root.left, level + 1)
        count(root, 0)
        return res