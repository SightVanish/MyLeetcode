/*
 * @Author: your name
 * @Date: 2021-09-12 17:07:27
 * @LastEditTime: 2021-09-12 20:05:28
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ21.cpp
 */
#include<iostream>
#include<vector>
#include<typeinfo>
#include <algorithm>
#include<stack>
using namespace std;
class Solution {
public:
    bool IsPopOrder(vector<int> pushV,vector<int> popV) {
        int p1 = 0, p2 = 0;
        stack<int> s;
        while (p1<pushV.size() && p2<popV.size())
        {
            if (s.empty())    s.push(pushV[p1++]);
            else
            {
                if (s.top()==popV[p2])
                {
                    s.pop();
                    p2++;
                }
                else
                {
                    s.push(pushV[p1++]);
                }
            }
        }
        if (p1>=pushV.size() && p2<popV.size())
        {
            while(s.top()==popV[p2])
            {
                s.pop();
                p2++;
                if(p2>=popV.size())    break;
            }
        }
        return s.empty();
    }
};