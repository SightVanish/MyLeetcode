"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        while l1 and l2:
            if l1.next is None:
                tmp = l1
            l1.val += l2.val
            l1 = l1.next
            l2 = l2.next
        if l2 and l1 is None:
            tmp.next = l2
        
        carry = 0
        l1 = head
        while l1:
            if l1.next is None:
                tmp = l1
            l1.val += carry
            carry = 0
            if l1.val >= 10:
                carry = 1
                l1.val -= 10
            l1 = l1.next
        if carry:
            tmp.next = ListNode(1)

        return head
    


p1 = ListNode(2)
p2 = ListNode(4)
p3 = ListNode(3)

p4 = ListNode(5)
p5 = ListNode(6)
p6 = ListNode(4)

p1.next=p2
p2.next=p3

p4.next=p5
p5.next=p6
s = Solution()
head = s.addTwoNumbers(p1, p4)
while head:
    print(head.val, end=' ')
    head = head.next
print('')