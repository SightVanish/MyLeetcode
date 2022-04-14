# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param listNode ListNode类 
# @return int整型一维数组
#
class Solution:
    def printListFromTailToHead(self , listNode: ListNode) -> List[int]:
        # write code here
        res = []
        pNode = listNode
        while (pNode != None):
            res.append(pNode.val)
            pNode = pNode.next
        res.reverse()
        return res