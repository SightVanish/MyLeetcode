/*
 * @Description: 
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-02 22:35:27
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-05 19:31:59
 * @FilePath: /Leetcode/task122.cpp
 */
// You are given an array prices where prices[i] is the price of a given stock on the ith day.

// Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

// Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <map>
#include <numeric>
using namespace std;

// my solution
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        bool canbuy=1;
        int profit=0;
        int hold=0;
        for(int i=0;i<prices.size();i++){
            if((i+1)==prices.size()){
                if(!canbuy){
                    profit+=prices[i]-hold;
                }
                break;
            }
            if(canbuy){
                //buy
                if(prices[i+1]>prices[i]){
                    cout<<"buy: "<<prices[i]<<endl;
                    canbuy=0;
                    hold=prices[i];
                }
            }
            else{
                //sell
                if(prices[i+1]<prices[i]){
                    cout<<"sell: "<<prices[i]<<endl;
                    canbuy=1;
                    profit+=prices[i]-hold;
                    hold=0;
                }
            }
        }
        return profit;
    }
};

// good solution--greedy
class Solution_1 {
public:
    int maxProfit(vector<int>& prices) {   
        int ans = 0;
        int n = prices.size();
        for (int i = 1; i < n; ++i) {
            ans += max(0, prices[i] - prices[i - 1]);//前后相减为正
        }
        return ans;
    }
};

// good solution--dynamic programming
// dp[i][0] 为第i天交易后未持有股票的最大收益(max(前一天未持有最大收益，前一天持有但是卖掉了最大收益))
// dp[i][1] 为第i天交易后持有股票的最大收益(max(前一天持有最大收益，前一天未持有但是今天买入最大收益))
class Solution_2 {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int dp0 = 0, dp1 = -prices[0]; 
        for (int i = 1; i < n; ++i) {
            int newDp0 = max(dp0, dp1 + prices[i]);
            int newDp1 = max(dp1, dp0 - prices[i]);
            dp0 = newDp0;
            dp1 = newDp1;
        }
        return dp0;
    }
};


int main(){
    vector<int> l;
    l.push_back(7);
    l.push_back(1);
    l.push_back(5);
    l.push_back(3);
    l.push_back(6);
    l.push_back(4);
    Solution s;
    
    cout<<s.maxProfit(l)<<endl;
    return 0;
}