# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head, tail):
        if head is None:
            return head, head
        if head.next is None:
            return head, head
        new_head, new_tail = self.reverseList(head.next, tail)
        head.next = None
        new_tail.next = head
        return new_head, head

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
head, tail = s.reverseList(p1, p5)
while head is not None:
    print(head.val)
    head = head.next