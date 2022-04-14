/*
 * @Description: easy
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-15 20:39:34
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-15 20:57:06
 * @FilePath: /Leetcode/task167.cpp
 */

// Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

// Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.

// The tests are generated such that there is exactly one solution. You may not use the same element twice.


#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <stack>
#include <numeric>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> result;
        // 使用双指针--一头一尾（前提是numebrs已经排序好）
        int i=0;
        int j=numbers.size()-1;
        while(i!=j){
            if ((numbers[i]+numbers[j])<target){
                i+=1;
            }
            else if ((numbers[i]+numbers[j])>target){
                j-=1;
            }
            else{
                break;
            }
        }
        if (i!=j){
            result.push_back(i+1);
            result.push_back(j+1);
        }
        return result;
    }
};

int main(){
    vector<int> i;
    i.push_back(2);
    i.push_back(7);
    i.push_back(11);
    i.push_back(15);
    Solution s;
    
    cout<<s.twoSum(i, 9)[1]<<endl;
    return 0;
}