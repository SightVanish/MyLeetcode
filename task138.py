# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
from typing import Optional
class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        history = {None: None}
        root = Node(0)
        p1, p2 = root, head
        while p2 is not None:
            p1.next = Node(p2.val)
            history[p2] = p1.next
            p1, p2 = p1.next, p2.next
        while head is not None:
            history[head].random = history[head.random]
            head = head.next
        return root.next