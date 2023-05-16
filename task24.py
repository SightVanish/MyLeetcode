"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        tmp = head.next
        head.next = tmp.next
        tmp.next = head
        if head.next: head.next = self.swapPairs(head.next)
        return tmp

p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p1.next=p2
p2.next=p3
p3.next=p4

s = Solution()
head = s.swapPairs(p1)
while head:
    print(head.val, end=' ')
    head = head.next
print('')