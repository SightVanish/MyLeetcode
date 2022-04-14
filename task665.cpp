/*
 * @Description: meduim
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-06 21:47:37
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-06 22:08:05
 * @FilePath: /Leetcode/.vscode/task665.cpp
 */

// Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

// We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <numeric>
using namespace std;

class Solution {
public:
    // 如果将nums[i]缩小，可能会导致其无法融入前面已经遍历过的非递减子数列；--需要尽可能不放大nums[i + 1]，这样会让后续非递减更困难；
    // 如果将nums[i + 1]放大，可能会导致其后续的继续出现递减；--如果缩小nums[i]，但不破坏前面的子序列的非递减性；
    bool checkPossibility(vector<int> &nums) {
        if (nums.size() == 1)   return true;
        bool flag = nums[0] <= nums[1] ? true : false; // 标识是否还能修改-即是否递减>=1
        for (int i = 1; i < nums.size() - 1; i++) // 因为考虑前后，故需要略过头尾
        {
            if (nums[i] > nums[i + 1])  // 出现递减
            {
                if (flag)   // 如果还有修改机会，进行修改
                {
                    if (nums[i + 1] >= nums[i - 1])// 修改方案1
                        nums[i] = nums[i + 1];
                    else                            // 修改方案2--必须改nums[i + 1]
                        nums[i + 1] = nums[i];      
                    flag = false;                   // 用掉唯一的修改机会
                }   
                else        // 没有修改机会，直接结束
                    return false;
            }
        }
        return true;
    }
};
