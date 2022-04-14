/*
 * @Description: meduim
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-07 11:30:05
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-15 18:40:48
 * @FilePath: /Leetcode/task1711.cpp
 */

// A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

// You can pick any two different foods to make a good meal.

// Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.

// Note that items with different indices are considered different even if they have the same deliciousness value.

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

// A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

// You can pick any two different foods to make a good meal.

// Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.

// Note that items with different indices are considered different even if they have the same deliciousness value.

class Solution {
public:
    static constexpr int MOD = 1000000007;

    int countPairs(vector<int>& deliciousness) {
        int maxVal = *max_element(deliciousness.begin(), deliciousness.end());
        int maxSum = maxVal * 2; // 最大可能的值
         
        int pairs = 0;
        unordered_map<int, int> mp;
        int n = deliciousness.size();
        
        for (auto& val : deliciousness) { // go through all elements
            
            for (int sum = 1; sum <= maxSum; sum <<= 1) { // <<= is equivalent to *=2
                int count = mp.count(sum - val) ? mp[sum - val] : 0; // .cout() returns the existence of an element
                // count is the number of the item that can form a power of 2 with val
                // it is aimed to aviod repeating number
                pairs = (pairs + count) % MOD;
            }
            mp[val]++;
        }
        return pairs;
    }
};





int main()
{
    // vector<int> k;
    // k.push_back(1);
    // k.push_back(1);
    // k.push_back(1);
    // k.push_back(3);
    // k.push_back(3);
    // k.push_back(3);
    // k.push_back(7);
    // k.push_back(7);
    // k.push_back(7);

    // Solution s;
    int s=1;
    s<<=1;
    cout<<s<<endl;

    s<<=1;
    s<<=1;
    cout<<s<<endl;

    
}