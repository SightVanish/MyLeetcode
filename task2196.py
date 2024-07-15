# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        if not descriptions: return 
        parents = {descriptions[0][0]: None}
        childrens = {}
        for p, c, l in descriptions:
            parents[c] = p
            childrens[(p, l)] = c
        root = descriptions[0][0]
        print(parents)
        while parents[root] is not None: root = parents[root]
        root = TreeNode(root)
        stack = [root]
        while stack:
            p = stack.pop()
            if (p.val, 1) in childrens: 
                left = TreeNode(childrens[(p.val, 1)])
                p.left = left
                stack.append(left)
            if (p.val, 0) in childrens:
                right = TreeNode(childrens[(p.val, 0)])
                p.right = right
                stack.append(right)
        return root

s = Solution()
p = s.createBinaryTree([[39,70,1],[13,39,1],[85,74,1],[74,13,1],[38,82,1],[82,85,1]])
print(p.val, p.left.val, p.right)
                

        
