"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
"""


















from typing import List
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: Node) -> List[int]:
        if root is None: return []
        tree = [root]
        res = []
        while tree:
            res.append(tree[0].val)
            if tree[0].children:
                tree = tree[0].children + tree[1:]
            else:
                tree = tree[1:]
        return res

p1 = Node(1)
p2 = Node(3)
p3 = Node(2)
p4 = Node(4)
p5 = Node(5)
p6 = Node(6)
p1.children = [p2, p3, p4]
p3.children = [p5, p6]

s = Solution()

print(s.preorder(p1))
