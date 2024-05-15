# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # l is the first node left to Node[left]
        if left == 1: l = ListNode(0, head)
        else:
            l = head
            for _ in range(1, left - 1): l = l.next
        pre, end, curr, next = l.next, l.next, None, None
        for _ in range(right - left):
            curr, next = pre.next, pre.next.next
            curr.next = pre
        l.next = curr
        end.next = next
        while head: 
            print(head.val)
            head = head.next
        return head

            
p1 = ListNode(5)
s = Solution()
print(s.reverseBetween(p1, 1, 1))