# follow task92 to handle this task
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printNodes(head: ListNode):
    while head: 
        print(head.val)
        head = head.next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: return None 
        p, num = head, 0
        while p:
            num += 1
            p = p.next
        dummy = ListNode(0, head)
        end, pre, curr, next = dummy, dummy, dummy.next, dummy.next.next
        for _ in range(num // k):
            for _ in range(k - 1):
                curr.next, pre, curr, next = pre, curr, next, next.next
            new_end, curr.next, end.next.next, end.next = end.next, pre, next, curr
            if new_end.next: end, pre, curr, next = new_end, new_end, new_end.next, new_end.next.next
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
printNodes(s.reverseKGroup(p1, 2))