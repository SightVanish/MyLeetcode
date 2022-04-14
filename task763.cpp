/*
 * @Description: 
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-02 20:39:43
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-02 22:35:42
 * @FilePath: /Leetcode/task763.cpp
 */
// You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

// Return a list of integers representing the size of these parts.

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
    vector<int> partitionLabels(string s) {
        map<char,vector<int>> m;
        vector<int> bb(2,-1);
        for (auto c : s){
            m[c]=bb;
        }    
        for (int i=0; i<s.size();i++){
            if(m[s[i]][0]==-1){
                m[s[i]][0]=i;
                m[s[i]][1]=i;
            }
            else{
                m[s[i]][1]=i;
            }
        }
        vector<vector<int> > ss;
        for (map<char,vector<int> >::iterator it=m.begin();it!=m.end();it++){
            ss.push_back(it->second);
        }
        sort(ss.begin(), ss.end(),[](vector<int>&a, vector<int>&b){return a[0]<b[0];});
        vector<int> result;
        int b=ss[0][0];
        int e=ss[0][1];
        for (int i=1;i<ss.size();i++){
            if(ss[i][0]<=e){
                e=max(e,ss[i][1]);
            }
            else{
                result.push_back(e-b+1);
                b=ss[i][0];
                e=ss[i][1];
            }
        }
        result.push_back(e-b+1);

        return result;
    }
};

// good solution
class Solution_1 {
public:
    vector<int> partitionLabels(string s) {
        int last[26];
        int length = s.size();
        for (int i = 0; i < length; i++) {
            last[s[i] - 'a'] = i; // the last time this character appears
        }

        vector<int> partition;
        int start = 0, end = 0;
        for (int i = 0; i < length; i++) {
            end = max(end, last[s[i] - 'a']); // the last time of the former&current character appears
            if (i == end) { // all characters are covered
                partition.push_back(end - start + 1);
                start = end + 1;
            }
        }
        return partition;
    }
};

int main(){
    cout<<'b' - 'a'; // =1
    return 0;
}