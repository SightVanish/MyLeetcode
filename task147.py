# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        pre_head = ListNode(float('-inf'), head)
        p = q = pre_head
        curr = head
        while curr:
            # print(pre_head.next.val, pre_head.next.next.val, pre_head.next.next.next.val, pre_head.next.next.next.next.val)

            # insertion part
            # handle special case
            if q.val <= curr.val:
                # do nothing
                q = curr
            else:
                
                q.next = curr.next # store curr.next
                while p.next and p.next.val < curr.val and p is not q:
                    p = p.next

                # if curr.val == 1:
                #     print(p.val, q.val)
                curr.next = p.next
                p.next = curr
            p = pre_head
            curr = q.next

        return pre_head.next

p1 = ListNode(4)
p2 = ListNode(2)
p3 = ListNode(1)
p4 = ListNode(3)

p1.next = p2
p2.next = p3
p3.next = p4

s = Solution()
p = s.insertionSortList(p1)

while p:
    print(p.val, end=' ')
    p = p.next