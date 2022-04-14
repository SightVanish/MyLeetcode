/*
 * @Author: your name
 * @Date: 2021-09-12 17:07:23
 * @LastEditTime: 2021-09-12 19:45:13
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ20.cpp
 */
class Solution {
public:
    void push(int value) {
        s.push(value);
        if (mins.empty())    mins.push(value);
        else
        {
            if (value<=mins.top())    mins.push(value); // 核心在于仅当valu<mins顶时才push，保证pop到minstop之前对minstop的次小值不会产生影响
        }
    }
    void pop() {
        int c = s.top();
        s.pop();
        if(c==mins.top())    mins.pop();
    }
    int top() {
        return s.top();
    }
    int min() {
        return mins.top();
    }
    stack<int> s;
    stack<int> mins;
};