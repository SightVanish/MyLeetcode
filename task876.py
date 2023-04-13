"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
"""
from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = head, head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        if p2.next is None:
            return p1
        if p2.next.next is None:
            return p1.next



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printListnode(head):
    while head is not None:
        print(head.val)
        head = head.next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        i = j = head
        while j is not None and j.next is not None:
            print('yes')
            i = i.next
            j = j.next.next
        return i

s = Solution()
p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p5 = ListNode(5)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5

p = s.middleNode(p1)
printListnode(p)
