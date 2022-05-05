# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = headA
        B = headB

        while A != B:
            if A != None:
                A = A.next
            else:
                A = headB
            if B != None:
                B = B.next
            else:
                B = headA
        # A == B
        return A

# if there is an intersection node, A will meet B; else A and B will both be None in the end.