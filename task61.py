from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        p, num = head, 1 # p is the end node
        while p.next:
            num += 1
            p = p.next
        k = k % num
        if k == 0: return head
        dummy = ListNode(0, head)
        pre, curr, next = dummy, head, head
        for _ in range(k): next = next.next
        while next: pre, curr, next = pre.next, curr.next, next.next
        p.next, dummy.next, pre.next = head, curr, None
        return dummy.next


p = ListNode(1)
s = Solution()
print(s.rotateRight(p, 0).val)

