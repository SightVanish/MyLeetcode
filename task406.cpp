/*
 * @Description: medium
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-05 20:03:30
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-06 21:34:19
 * @FilePath: /Leetcode/task406.cpp
 */

// You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

// Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <map>
#include <unordered_map>
#include <stack>
#include <numeric>
using namespace std;


class Solution {
public:
    // 判别方法--先按身高降序排列，然后按前面的人数升序排列
    static bool cmp(const vector<int> a, const vector<int> b) {
        if (a[0] == b[0]) return a[1] < b[1];
        return a[0] > b[0];
    }
    
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        // 保证大的值先插入，保证前面数字小的先插入
        sort(people.begin(), people.end(), cmp); // [[7,0], [7,1], [6,1], [5,0], [5,2]，[4,4]]

        // 注意此处que需要另开--由于vector插入效率低，此处使用list
        list<vector<int>> que;

        for (int i = 0; i < people.size(); i++) {
            int position = people[i][1];
            int count=position;
            list<vector<int>>::iterator it = que.begin();
            while (count!=0){
                it++;
                count--;
            }
            que.insert(it, people[i]);
        }
        return vector<vector<int>>(que.begin(), que.end()); // note: 此处为用list初始化vector的方法之一
    }
};


int main(){
    // [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
    vector<vector<int>> i;
    vector<int> j;
    j.__emplace_back(6);
    j.__emplace_back(0);   
    i.__emplace_back(j);
    
    j[0]=5; j[1]=0; i.__emplace_back(j);
    j[0]=4; j[1]=0; i.__emplace_back(j);
    j[0]=3; j[1]=2; i.__emplace_back(j);
    j[0]=2; j[1]=2; i.__emplace_back(j);
    j[0]=1; j[1]=4; i.__emplace_back(j);
    
    
    vector<vector<int>> p;
    p=i;
    p[0][0]=10;
    Solution s;
    cout<<"[";
    for (auto m : s.reconstructQueue(i)){
        cout<<"["<<m[0]<<", "<<m[1]<<"]";
    }
    cout<<"]";

    
    return 0;
}