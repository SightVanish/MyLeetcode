/*
 * @Author: your name
 * @Date: 2021-09-12 11:54:49
 * @LastEditTime: 2021-09-12 11:54:50
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ6.cpp
 */

class Solution {
public:
    int minNumberInRotateArray(vector<int> rotateArray) {
        int min = rotateArray[0];
        for(auto i:rotateArray)
        {
            if(min>i)    return i;
            else    min=i;
        }
        return rotateArray[0];
    }
};