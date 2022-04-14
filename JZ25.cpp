/*
 * @Author: your name
 * @Date: 2021-09-12 17:07:42
 * @LastEditTime: 2021-09-12 22:22:03
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ25.cpp
 */

/*
struct RandomListNode {
    int label;
    struct RandomListNode *next, *random;
    RandomListNode(int x) :
            label(x), next(NULL), random(NULL) {
    }
};
*/
class Solution {
public:
    RandomListNode* Clone(RandomListNode* pHead) {
        if(pHead==nullptr)    return nullptr;
        auto current = pHead;
        // create new list with no random reference
        while(current!=nullptr)
        {
            RandomListNode* friendNode = new RandomListNode(current->label);
            // create new reference
            friendNode->next = current->next;            
            current->next = friendNode;
            current=friendNode->next;
        }
        
        current=pHead;
        while(current!=nullptr)
        {
            current->next->random = current->random==nullptr?nullptr:current->random->next; // you have to check nullptr here
            current=current->next->next;
        }
        
        current = pHead;
        auto ret = current->next;
        while(current!=nullptr)
        {
            auto cloneNode = current->next;
            current->next = cloneNode->next;
            cloneNode->next = cloneNode->next==nullptr?nullptr:cloneNode->next->next;
            current = current->next;
        }
        return ret;
    }
};