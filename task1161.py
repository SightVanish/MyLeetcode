"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
"""












from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curr_level = []
        next_level = [root]
        res, level, total = 0, 0, -float('inf')
        while next_level:

            curr = 0
            level += 1
            curr_level = next_level
            next_level = []
            for i in curr_level:
                curr += i.val
                if i.left: next_level.append(i.left)
                if i.right: next_level.append(i.right)
        
            if curr > total: 
                res = level
                total = curr
        return res


p1 = TreeNode(-100)
p2 = TreeNode(-200)
p3 = TreeNode(-300)
p4 = TreeNode(-20)
p5 = TreeNode(-5)
p6 = TreeNode(-10)

p1.left=p2
p1.right=p3
p2.left = p4
p2.right=p5
p3.left=p6

s = Solution()
print(s.maxLevelSum(p1))
