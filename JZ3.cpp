/*
 * @Author: your name
 * @Date: 2021-09-11 22:32:10
 * @LastEditTime: 2021-09-11 22:35:13
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ3.cpp
 */
#include<iostream>
#include<vector>
#include<typeinfo>
using namespace std;


struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
        val(x), next(NULL) {
    }
};

class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        vector<int> ans;
//         for (auto i = head;i!=nullptr;i=i->next)
//         {
//              ans.insert(ans.begin(), i->val);
//         }
        auto i = head;
        while(i!=nullptr)
        {
            ans.push_back(i->val);
            i=i->next;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};