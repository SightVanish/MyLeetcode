from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        dummy = ListNode(0, head)
        pre, curr, next = dummy, dummy.next, dummy.next.next
        while next:
            if next.val == curr.val:
                while next and next.val == curr.val: next = next.next
                pre.next, curr, next = next, next, next.next if next else next
            else: 
                pre, curr, next = pre.next, curr.next, next.next
        return dummy.next
        
