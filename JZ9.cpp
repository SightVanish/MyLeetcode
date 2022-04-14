/*
 * @Author: your name
 * @Date: 2021-09-12 12:02:02
 * @LastEditTime: 2021-09-12 12:03:02
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ9.cpp
 */

// f(1) = f(0)
// f(2) = f(1)+f(0)
// f(3) = f(0)+f(1)+f(2)
// f(n-1) = f(0)+...+f(n-2)+f(n-1)
// f(n) = f(0)+...+f(n-2)+f(n-1) = f(n-1)+f(n-1) = 2*f(n-1)


class Solution {
public:
    int jumpFloorII(int number) {
        if(number<=1)    return 1;
        else    return 2*jumpFloorII(number-1);
    }
};