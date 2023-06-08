"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, p2, p3 = head, head, head
        for i in range(n):
            p2 = p2.next
            if p2 is None and i != n-1: return None
        while p2:
            p3 = p1
            p1 = p1.next
            p2 = p2.next
        if p1 == head: return p1.next
        p3.next = p1.next
        return head