# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printNode(p):
    while p:
        print(p.val, end = ' ')
        p = p.next
    print('')   
class Solution:
    def findMid(self, head):
        if head is None or head.next is None:
            return head

        p1 = p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        return p1
        
    def mergeList(self, p1, p2):
        # p1 is longer/equal to p2
        new_head = ListNode(0)
        p = new_head
        while p1 and p2:
            # print(p1.val, p2.val)
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next

        if p1:
            p.next = p1
        elif p2:
            p.next = p2
        return new_head.next

    def sortList(self, head):
        if head is None or head.next is None:
            return head
        # find mid
        mid = self.findMid(head)
        # break chain
        p = head
        while p.next != mid:
            p = p.next
        p.next = None
        
        # sort two list
        mid = self.sortList(mid)
        head = self.sortList(head)
        # merge two lists
        new_head = self.mergeList(mid, head)

        return new_head
s = Solution()
p1 = ListNode(1)
p2 = ListNode(3)
p3 = ListNode(5)

p4 = ListNode(2)
p5 = ListNode(4)

p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5

# p = s.mergeList(p1, p4)
p = s.sortList(p1)
printNode(p)
