/*
 * @Description: easy
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-15 20:58:37
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-15 22:04:49
 * @FilePath: /Leetcode/task66.cpp
 */
// You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

// Merge nums1 and nums2 into a single array sorted in non-decreasing order.

// The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


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
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i=m-1;
        int j=n-1;
        int p=m+n-1;
        while(i>=0 && j>=0){
            if(nums1[i]>nums2[j]){
                nums1[p]=nums1[i];
                i--;
            }
            else{
                nums1[p]=nums2[j];
                j--;
            }
            p--;
        }
        // if j<0, we do not care
        while(j>=0){
            nums1[p--]=nums2[j--];
        }
    }
};