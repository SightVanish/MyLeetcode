/*
 * @Author: your name
 * @Date: 2021-09-12 15:31:45
 * @LastEditTime: 2021-09-12 15:31:45
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ14.cpp
 */
/**
 * struct ListNode {
 *	int val;
 *	struct ListNode *next;
 *	ListNode(int x) : val(x), next(nullptr) {}
 * };
 */
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param pHead ListNode类 
     * @param k int整型 
     * @return ListNode类
     */
    ListNode* FindKthToTail(ListNode* pHead, int k) {
        // write code here
        int depth = 0;
        auto p1 = pHead;
        auto p2 = pHead;
        if (!pHead)    return nullptr;
        k=k-1;
        while(k!=0)
        {
            p1=p1->next;
            k--;
            if (p1==nullptr)    return nullptr;
        }
        while(p1->next!=nullptr)
        {
            p1=p1->next;
            p2=p2->next;
        }
        return p2;
    }
};