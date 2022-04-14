/*
 * @Description: 
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-02 11:41:49
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-02 11:59:57
 * @FilePath: /Leetcode/task1833.cpp
 */

// It is a sweltering summer day, and a boy wants to buy some ice cream bars.

// At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

// Return the maximum number of ice cream bars the boy can buy with coins coins.

// Note: The boy can buy the ice cream bars in any order.
#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <unordered_map>
#include <numeric>
using namespace std;

class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        sort(costs.begin(), costs.end());
        int count=0;
        for (int i=0; i<costs.size(); i++){
            if (coins>=costs[i]){
                coins-=costs[i];
                count+=1;
            }
            else{
                break;
            }
        }
        return count;
    }
};

int main()
{
    vector<int> costs;
    costs.push_back(1);
    costs.push_back(6);
    costs.push_back(3);
    costs.push_back(1);
    costs.push_back(2);
    costs.push_back(5);
    int coins = 20;
    Solution s;
    cout<<s.maxIceCream(costs, coins);
    return 0;
}