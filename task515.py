"""
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).
"""

from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        current, next, ans = [root], [], []
        while current:
            m = -float('inf')
            while current:
                if current[0].val > m: m = current[0].val
                if current[0].left: next.append(current[0].left)
                if current[0].right: next.append(current[0].right)
                current = current[1:]
            ans.append(m)
            current, next = next, []
        return ans

s = Solution()
print(s.largestValues([]))




