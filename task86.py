from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small, large = ListNode(0, head), ListNode(0, head)
        p1, p2, p = small, large, head
        while p:
            if p.val < x: p1.next, p1, p = p, p, p.next
            else: p2.next, p2, p = p, p, p.next
        if p2 != large: p1.next, p2.next = large.next, None # if p2 = large, this will cause a circle
        return small.next

p = ListNode(1)
s = Solution()
print(s.partition(p, 2))
