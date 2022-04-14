/*
 * @Description: hard
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-16 16:08:08
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-16 16:08:57
 * @FilePath: /Leetcode/task76.cpp
 */

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

// Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

// The testcases will be generated such that the answer is unique.

// A substring is a contiguous sequence of characters within the string.


class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map <char, int> need;
        // count the number of t
        for (auto i:t){
            need[i]++;
        }

        int needCount = t.size(); // how many number we need to count

        int l=0,r=0,start=0,size=INT_MAX; // l,r is the sliding window--start,size is the output we want
        while(r<s.size()){
            // consider the most right char
            auto c=s[r]; 
            if (need[c]>0)  needCount--; // c is what we need
            need[c]--; // what ever we need it or not, all --
            
            // the sliding window has all we need
            if (needCount==0){
                // while we can l++
                while(l<r && need[s[l]]<0){
                    need[s[l++]]++;
                }
                // record the result
                if ((r-l+1)<size){
                    size=r-l+1;
                    start=l;
                }

                // l++ to continue
                need[s[l]]++;
                l++;
                needCount++;
            }
            
            r++;
        }
        return size==INT_MAX ? "" : s.substr(start, size); // if size==INI_MAX, return ""
    }
};
