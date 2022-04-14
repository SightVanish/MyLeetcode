/*
 * @Author: your name
 * @Date: 2021-09-12 15:31:58
 * @LastEditTime: 2021-09-12 15:36:59
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ15.cpp
 */

/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* ReverseList(ListNode* pHead) {
        ListNode* before = nullptr;
        auto current = pHead;
        auto next = pHead->next;
        while(current!=nullptr)
        {
            current->next = before;
            before = current;
            current = next;
            next = next->next;
        }
        return before;
    }
};