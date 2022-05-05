class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printListnode(head):
    while head is not None:
        print(head.val, end=' ')
        head = head.next
    print('')
class Solution1:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodeList = []
        p = head
        while p is not None:
            nodeList.append(p)
            p = p.next
            
        i = 0
        j = len(nodeList) - 1
        while i <= j:
            nodeList[i].next = nodeList[j]
            i += 1
            nodeList[j].next = nodeList[i]
            j -= 1

        nodeList[j + 1].next = None
        # print(i, j)
        return head


class Solution:
    def midList(self, head):
        i = j = head
        while j is not None and j.next is not None:
            i = i.next
            j = j.next.next
        if j is None:
            return i
        else:
            return i.next

    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        head_next = head.next
        new_head = self.reverseList(head_next)
        head.next = None
        head_next.next = head
        return new_head



    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head

        mid = self.midList(head)
        p = head
        while p.next != mid:
            p = p.next
        p.next = None

        p1 = head
        p2 = self.reverseList(mid)

        # merge two list
        while p1 is not None and p2 is not None:
            p1_next = p1.next
            p2_next = p2.next
            p1.next = p2
            p2.next = p1_next

            p1 = p1_next
            p2 = p2_next

        return head
        

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

p = s.reorderList(p1)
printListnode(p)

