/*
 * @Author: your name
 * @Date: 2021-09-12 12:19:49
 * @LastEditTime: 2021-09-12 12:20:54
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ10.cpp
 */

class Solution {
public:
    int rectCover(int number) {
        if (number==0)    return 0;
        if (number<=2)    return number; // 关键在于number=2时结果等于2 与number=0时结果等于0的逻辑相冲突，因此两个都单独拿出来处理即可
        else    return rectCover(number-1)+rectCover(number-2);
    }
};