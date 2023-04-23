"""
Given the root of a binary tree, return the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels.
The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.
It is guaranteed that the answer will in the range of a 32-bit signed integer.
Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
"""















from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 1
        layer1 = [root]
        layer2 = []
        while layer1 and not all(i is None for i in layer1):
            # for i in layer1:
            #     if i: print(i.val, end=' ')
            #     else: print('None', end=' ')
            # print('')
            
            i, j = 0, len(layer1)-1
            while layer1[i] is None: i += 1
            while layer1[j] is None: j -= 1
            res = max(res, j-i+1)
            for i in range(len(layer1)):
                if layer1[i]: layer2 += [layer1[i].left, layer1[i].right]
                else:
                    layer2 += [None, None]
            layer1 = layer2
            layer2 = []
        return res


p1 = TreeNode(1)
p2 = TreeNode(3)
p3 = TreeNode(2)
p4 = TreeNode(5)
p5 = TreeNode(9)
p6 = TreeNode(6)
p7 = TreeNode(7)

p1.left = p2
p1.right = p3
p2.left = p4
p4.left = p5
p3.right = p6
p6.left = p7

s = Solution()
print(s.widthOfBinaryTree(p1))