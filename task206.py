"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        p1, p2 = head, head.next
        while p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        head.next = None
        return p1

p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p1.next = p2
p2.next = p3
p3.next = p4

s = Solution()
p = s.reverseList(p1)
while p:
    print(p.val)
    p = p.next