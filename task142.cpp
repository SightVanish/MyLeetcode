/*
 * @Description: medium
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-15 22:05:13
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-16 16:07:33
 * @FilePath: /Leetcode/task142.cpp
 */

// Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

// Notice that you should not modify the linked list.

#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <stack>
#include <numeric>
using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// Floyd 判圈法--slow走一步，fast走两步，最终相遇距离圈起点长度+n圈为圈起点距离起点长度（仅使用于题目中这种特殊情况）
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow = head, *fast = head;
        // it should be do first--slow=fast now
        do{
            // if there is no cycle
            if(fast==nullptr || fast->next==nullptr){
                return nullptr;
            }
            fast = fast->next->next;
            slow = slow->next;
        }while (fast!=slow);
                // at this moment, fast=slow
        fast = head;
        while (fast != slow){
            slow = slow->next;
            fast = fast->next;
        }
        return fast;
    }

};

int main(){
    ListNode s1(3);
    ListNode s2(2);
    ListNode s3(0);
    ListNode s4(-4);
    s1.next=&s2;
    s2.next=&s3;
    s3.next=&s4;
    s4.next=&s2;
    
    Solution s;
    int a = s.detectCycle(&s1)->val;
    cout<<a<<endl;
    

    return 0;
}