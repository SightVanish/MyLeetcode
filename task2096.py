# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
# memory limit exceeded
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # find the lowest common ancestor
        def findAncestor(root: Optional[TreeNode]):
            if root.val == startValue or root.val == destValue: return root
            left, right = None, None
            if root.left: left = findAncestor(root.left)
            if root.right: right = findAncestor(root.right)
            if left and right: return root
            else: return left or right
        # find the path from root to target
        def findPath(root: Optional[TreeNode], target: int, path: Optional[List]):
            if not root: return None
            if root.val == target: return path
            left_path = findPath(root.left, target, path + ['L'])
            if left_path: return left_path
            right_path = findPath(root.right, target, path + ['R'])
            if right_path: return right_path
            return None
        ancestor = findAncestor(root)
        left_path = findPath(ancestor, startValue, [])
        right_path = findPath(ancestor, destValue, [])
        return 'U'*len(left_path) + ''.join(right_path)

# list in python is passed via reference -- save memory
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # find the path from root to target
        def findPath(root: Optional[TreeNode], target: int, path: Optional[List]):
            if not root: return False
            if root.val == target: return True
            if findPath(root.left, target, path): path.append('L')
            elif findPath(root.right, target, path): path.append('R')
            # print(root.val, path)
            return path
        
        left_path, right_path = [], []
        findPath(root, startValue, left_path)
        findPath(root, destValue, right_path)
        left_path.reverse()
        right_path.reverse()
        # remove the common prefix -- the ancestor
        i = 0
        while i < len(left_path) and i < len(right_path) and left_path[i] == right_path[i]: i += 1
        left_path = left_path[i:]
        right_path = right_path[i:]
        return 'U' * len(left_path) + ''.join(right_path)
    
p1 = TreeNode(5)
p2 = TreeNode(1)
p3 = TreeNode(2)
p4 = TreeNode(3)
p5 = TreeNode(6)
p6 = TreeNode(4)
p1.left = p2
p1.right = p3
p2.left = p4
p3.left = p5
p3.right = p6

s = Solution()
print(s.getDirections(p1, 3, 6))