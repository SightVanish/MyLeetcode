// Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

// Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

#include <iostream>
#include <vector>
#include <list>
#include <math.h>
#include <unordered_map>
using namespace std;
class Solution_1 {
public:
    int findContentChildren(vector<int>& children, vector<int>& cookies) {
        sort(children.begin(), children.end()); // sort from small to large
        sort(cookies.begin(), cookies.end());
        int child = 0, cookie = 0;
        while (child < children.size() && cookie < cookies.size()) {
            if (children[child] <= cookies[cookie]) ++child;
            ++cookie;
        }
        return child;
   }

};
