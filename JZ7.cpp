/*
 * @Author: your name
 * @Date: 2021-09-12 11:56:47
 * @LastEditTime: 2021-09-12 11:56:48
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ7.cpp
 */

class Solution {
public:
    int Fibonacci(int n) {
        if (n<=1)    return n;
        else    return Fibonacci(n-1)+Fibonacci(n-2);
    }
};