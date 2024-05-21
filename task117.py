# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return None
        curr, next = [root], []
        while curr:
            for i in curr: 
                if i.left: next.append(i.left)
                if i.right: next.append(i.right)
            for i in range(len(next) - 1): next[i].next = next[i + 1]
            if next: next[-1].next = None
            curr, next = next, []
        return root
        
