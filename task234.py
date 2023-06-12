"""
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.
Example 1:
Input: head = [1,2,2,1]
Output: true
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast, slow_pre = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, slow, slow_pre = slow_pre, slow.next, slow # this is only feasible in python
        if fast: slow = slow.next
        while slow:
            if slow.val != slow_pre.val: return False
            slow, slow_pre = slow.next, slow_pre.next
        return True

p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(2)
p4 = ListNode(1)
p1.next = p2
p2.next = p3
p3.next = p4

s = Solution()
print(s.isPalindrome(p1))