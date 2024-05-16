# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printNodes(head: ListNode):
    while head: 
        print(head.val)
        head = head.next
from typing import Optional
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None: return None 
        dummy = ListNode(0, head)
        pre = dummy # the first node left the Node[left]
        for _ in range(left - 1): pre = pre.next
        end, curr, next = pre, pre.next, pre.next.next
        for _ in range(right - left): curr.next, pre, curr, next = pre, curr, next, next.next
        curr.next, end.next.next, end.next = pre, next, curr
        return dummy.next
            
p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5

s = Solution()
printNodes(s.reverseBetween(p1, 2, 4))