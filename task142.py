"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""















from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next and head.next.next:
            slow, fast = head.next, head.next.next
        else: return None
        while slow != fast:
            if fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head


p1 = ListNode(3)
p2 = ListNode(2)
p3 = ListNode(0)
p4 = ListNode(-4)

p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p2

s = Solution()
print(s.detectCycle(p1).val)