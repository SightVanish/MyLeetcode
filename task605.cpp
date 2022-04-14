/*
 * @Description: 
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-02 16:44:56
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-02 20:06:54
 * @FilePath: /Leetcode/task605.cpp
 */

// You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

// Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <unordered_map>
#include <numeric>
using namespace std;

// 从头到尾进行遍历，判断每个位置时候可以种花，可以就种
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if (flowerbed.size()==1){
            if (n>1){
                return false;
            }
            else if (n==1){
                if (flowerbed[0]==0){
                    return true;
                }
                else{
                    return false;
                }
            }
            else if (n==0){
                return true;
            }
        }
        int m = 0;
        for(auto i=flowerbed.begin(); i!=flowerbed.end();i++){
            if (*i==1){
                m+=1;
            }
        }
        m+=n;
        for(auto i=flowerbed.begin(); i!=flowerbed.end();i++){
            if (i==flowerbed.begin()){
                if(*i==1 || *(i+1)==1){
                    continue;
                }
                else{
                    *i=1;
                }
            }
            else if(i+1==flowerbed.end()){
                if(*i==1 || *(i-1)==1){
                    continue;
                }
                else{
                    *i=1;
                }
            }
            else{
                if(*i==1 || *(i+1)==1 || *(i-1)==1){
                    continue;
                }
                else{
                    *i=1;
                }
            }
        }
        int k = 0;
        for(auto i=flowerbed.begin(); i!=flowerbed.end();i++){
            if (*i==1){
                k+=1;
            }
        }
        if (k>=m){
            return true;
        }
        else{
            return false;
        }
    }
};

// good solution
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // 每次跳两格
        for (int i = 0; i < flowerbed.size(); i += 2) {
            // 如果当前为空地
            if (flowerbed[i] == 0) {
                // 如果是最后一格或者下一格为空，则可以种
                if (i == flowerbed.size() - 1 || flowerbed[i + 1] == 0) {
                    n--;
                } else {
                    // 此时下一格A为1，则从下一格A+1开始跳两格，因为不能相邻，因此A+2必为0，利用此特性
                    i++;
                }
            }
        }
        return n <= 0;
    }
};

