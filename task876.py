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
