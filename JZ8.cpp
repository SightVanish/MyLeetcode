/*
 * @Author: your name
 * @Date: 2021-09-12 11:58:59
 * @LastEditTime: 2021-09-12 11:58:59
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ8.cpp
 */

class Solution {
public:
    int jumpFloor(int number) {
        if(number<=1)    return 1;
        if(number==2)    return 2;
        else    return jumpFloor(number-1)+jumpFloor(number-2);
    }
};