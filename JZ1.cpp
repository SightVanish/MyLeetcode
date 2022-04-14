/*
 * @Author: your name
 * @Date: 2021-09-11 21:53:19
 * @LastEditTime: 2021-09-11 22:04:36
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ1.cpp
 */

#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    bool Find(int target, vector<vector<int> > array) {
        int m = array.size();
        int n = array[0].size();
        int i = m-1;
        int j = 0;
        while(i>=0 && j<=n-1)
        {
            if(array[i][j]==target)    return true;
            else if(array[i][j]<target)    j++;
            else if(array[i][j]>target)    i--;
        }
        return false;
    }
};