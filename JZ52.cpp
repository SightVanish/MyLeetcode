// 两个链表的第一个相交
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

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        // two pointers
        ListNode *p1 = headA, *p2 = headB;
        // 两个pointer同时往后走
        // 如果同时到相交/结束返回正确结果
        // 如果不能同时达到，则会从另一个头开始遍历（最后总能保证同时在相交点相遇/最后不相交）
        while (p1!=p2){
            p1 = p1 ? p1->next:headB;
            p2 = p2 ? p2->next:headA;
        }
        return p1;
    }
};


