"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""
from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# O(n*k) while n is the length of linked list
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        lists = list(filter(lambda x: x is not None, lists))
        while(lists):
            min_node = min(lists, key= lambda x: x.val)
            i = lists.index(min_node)
            curr.next = lists[i]
            curr = lists[i]
            if min_node.next is None: 
                lists.remove(lists[i])
            else: lists[i] = lists[i].next
        return head.next

# Another solution is to use divid and conquer, breaking merge-k problems to meger-two problems
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge2Lists(self, list1, list2):
            head = ListNode(0)
            p, p1, p2 = head, list1, list2
            while p1 and p2:
                if p1.val < p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next
            if p1: p.next = p1
            elif p2: p.next = p2
            return head.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0: return None
        if n == 1: return lists[0]
        if n == 2: return self.merge2Lists(lists[0], lists[1])
        p1 = self.mergeKLists(lists[:n//2])
        p2 = self.mergeKLists(lists[n//2:])
        return self.merge2Lists(p1, p2)


p1 = ListNode(1)

s = Solution()
p = s.mergeKLists([None, p1])