/*
 * @Description: 
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-02 11:30:25
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-02 16:54:08
 * @FilePath: /Leetcode/task435.cpp
 */
#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <unordered_map>
#include <numeric>
using namespace std;

// Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int> >& intervals) {
        if (intervals.empty()) return 0; 
        int n = intervals.size();
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b){return a[1] < b[1];}); //按照结束时间进行排序
        int removed=0;
        int current_time=intervals[0][0];
        for (int i=0;i<intervals.size();i++){
            if (intervals[i][0]>=current_time){
                // take this event, update current_time
                current_time = intervals[i][1];
                
            }
            else{
                // skip this event
                removed+=1;
            }
        }
        return removed;
    }
};

int main(){
    // vector<vector<int> > a;
    // vector<int> b;
    // b.push_back(1);
    // b.push_back(2);
    // a.push_back(b);
    // b[0]=2;
    // b[1]=4;
    // a.push_back(b);
    // b[0]=1;
    // b[1]=3;
    // a.push_back(b);

    // Solution s;
    // cout<<s.eraseOverlapIntervals(a);

    // ----------testing----------
    vector<int> b;
    b.push_back(3);
    b.push_back(5);
    int a[10] = {1,3,5};
    // cout<<*max_element(a, a+10)<<endl; // note here the end is a+10
    // cout<<a<<endl;
    auto c=b.begin();
    cout<<*(c+1)<<endl;

    
    return 0;
}
