/*
 * @Description: 
 * @Author: LiWuchen
 * @Github: https://github.com/SightVanish
 * @Date: 2021-07-02 20:07:36
 * @LastEditors: LiWuchen
 * @LastEditTime: 2021-07-02 20:38:39
 * @FilePath: /Leetcode/task452.cpp
 */

// There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.

// An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.

// Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.

#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <unordered_map>
#include <numeric>
using namespace std;



//考虑所有气球中右边界位置最靠左的那一个，那么一定有一支箭的射出位置就是它的右边界（否则就没有箭可以将其引爆了）。当我们确定了一支箭之后，我们就可以将这支箭引爆的所有气球移除，并从剩下未被引爆的气球中，再选择右边界位置最靠左的那一个，确定下一支箭，直到所有的气球都被引爆。
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        // sort by the second element
        sort(points.begin(), points.end(),[](vector<int>&a, vector<int>&b){return a[1]<b[1];});
        vector<bool> blow(points.size(),0);
        int num=1;
        int pos=points[0][1]; // the position of the arrow
        for (const vector<int>& balloon: points) {
            if (balloon[0] > pos) {
                pos = balloon[1]; // the first one that cannot be shoot by this array
                ++num;
            }
        }
        return num;
    }
};
