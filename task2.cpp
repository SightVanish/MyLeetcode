/*You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.*/
#include <iostream>
#include <stdlib.h>
#include <stack>
#include <time.h>
#include <cstdlib>
using namespace std;
struct ListNode {
    int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

//This is my solution
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* Head = new ListNode(0);//create a list to store the value
        ListNode* iter = Head;
        int sum = 0;
        int carry = 0;//indicate whether we should carry in

        while(l1 != NULL || l2 != NULL){//while we can still add 
            sum = carry;//every time, you need to init sum first
            if(l1 != NULL){
                sum += l1->val;
                l1 = l1->next;
            }
            if(l2 != NULL){
                sum += l2->val;
                l2 = l2->next;
            }
            //decide whether we need to carry in
            carry = sum >= 10 ? 1 : 0;
            //the next node we need add to the answer
            iter->next = new ListNode(sum%10);//before: next = NULL, after: next = the address allocated
            iter = iter->next;//add new node to answer
        }
        if (carry == 1) iter->next = new ListNode(1);
        //as it is not convinent to deal with the first element of the List so we just free the head node
        ListNode* answer = Head->next;  
        free(Head);
        return answer;
    }
};

//a little bit more modification
/*
1.为了节省内存，只在已有的l1、l2节点上操作，结果最多增添一个ListNode节点保存进位->try to save memory
2.为了逻辑的方便，保留l1节点，如果l1较短，l1的尾结点指向l2剩余的节点，通过l1返回结果->also try to save memory
3.最坏情况下，总的遍历次数是两个链表的长度之后(length1+length2)，如果进位不是到达最后一个节点，提前退出，遍历次数会小于(length1+length2)，节省时间，时间复杂度o(n)。
主要逻辑：
从头开始同时遍历l1和l2，处理两个链表长度相等部分的节点之和，并记录l1的尾结点lTailNode，记录最后的进位iAdd
如果l1节点较多，且上一步的进位iAdd为0，直接return l1，否则继续用l1余下的节点和iAdd计算，直到结束
如果l2节点较多，将l1的尾节点指向l2的剩余节点的第一个节点。如果第一步的进位iAdd为0，直接return l1。否则继续用l2余下的节点和iAdd计算，直到结束
如果最后iAdd>0，新增一个节点，值为1。
return l1。
*/
class Solution_good {
public:
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2){
    if(l1==NULL && l2==NULL) return NULL; 
    if(l1==NULL) return l2; 
    if(l2==NULL) return l1; 

    ListNode* ltemp1 = l1;//if l1 = l1->next, there is no need to set another iterator
    ListNode* lTailNode = l1; //把所有结果都通过l1传递，保存l1的最后一个节点
    ListNode* ltemp2 = l2; 
    int iAdd = 0;
    int iValue = 0;
    //处理长度相等部分的节点
    while(ltemp1 && ltemp2)
    {
        iValue = ltemp1->val + ltemp2->val + iAdd;
        iAdd = iValue / 10; //since iValue must < 20 so we can use this method to get carry
        ltemp1->val = iValue % 10; 

        lTailNode = ltemp1;
        ltemp1 = ltemp1->next;
        ltemp2 = ltemp2->next;
    }   
    //above we are all same, so how to deal with extra nodes?-following
    //如果l1节点较多 
    if(ltemp1)
    {
        //如果无进位 直接return
        if(iAdd == 0)
        {
            return l1;
        }
        //处理进位
        while(ltemp1)
        {
            ltemp1->val = ltemp1->val + iAdd;//let last value++ and deal with carry
            if(ltemp1->val >= 10)
            {
                iAdd = ltemp1->val / 10;
                ltemp1->val = ltemp1->val % 10;
            }
            else
            {
                iAdd = 0;
                break;
            }
            lTailNode = ltemp1;//lTailNode = l1(before)                                                                     
            ltemp1 = ltemp1->next;
        }
    }
    else if(ltemp2) //如果l2较长，将l1尾部指向剩余的l2节点
    {
        lTailNode->next = ltemp2; //l1的尾节点指向l2的剩余部分
        //still we need to deal with carry 
        if(iAdd == 0)
        {
            return l1;
        }
        while(ltemp2)
        {
            ltemp2->val = ltemp2->val + iAdd;
            if(ltemp2->val >= 10)
            {
                iAdd = ltemp2->val / 10;
                ltemp2->val = ltemp2->val % 10;
            }
            else
            {
                iAdd = 0;
                break;
            }
            lTailNode = ltemp2;
            ltemp2 = ltemp2->next;
        }
    }
    //如果两个链表都同时到达尾部且进位不为0 或者长链表处理完 进位不为0
    if(iAdd > 0)
    {
        ListNode *pnew = new ListNode(iAdd);
        lTailNode->next = pnew;
    }
    return l1;
    }
};

int main(){
    srand(time(0));//set seed to get random number
    ListNode* Head = new ListNode(rand()%10);
    ListNode* iter = Head;
    for(int i = 0; i < 100000; i++){
        iter->next = new ListNode(rand()%10);
        iter = iter->next;
    }
    ListNode *Ans1;
    ListNode *Ans2;
    Solution s1;
    Solution_good s2;
    clock_t starttime1 = clock();
    Ans1 = s1.addTwoNumbers(Head,Head);
    clock_t endtime1 = clock();
    cout << endl << "This algorithm time usage is "<< (double)(starttime1-endtime1)/CLOCKS_PER_SEC << endl;
    
    clock_t starttime2 = clock();
    Ans2 = s2.addTwoNumbers(Head,Head);
    clock_t endtime2 = clock();
    cout << endl << "This algorithm time usage is "<< (double)(starttime2-endtime2)/CLOCKS_PER_SEC << endl;
    


    return 0;
}