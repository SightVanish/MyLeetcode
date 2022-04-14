// You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

// Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

// An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.

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

// my solution--use hash map to remember all the numbers we count
class Solution_1 {
public:
    bool isCovered(vector<vector<int>>& ranges, int left, int right) {
        unordered_map<int, int> m;
        for (vector<int> i:ranges){
            int l=i[0];
            int r=i[1];
            for (int j=l;j<=r;j++){
                m[j]=1;
            }
        }
        for (int i=left;i<=right;i++){
            if(!m.count(i)){
                return false;
            }
        }
        return true;
    }
};
