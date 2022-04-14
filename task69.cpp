//
//  main.cpp
//  task69
//
//  Created by 李戊辰 on 2021/8/8.
//
//Given a non-negative integer x, compute and return the square root of x.
//
//Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
//
//Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
#include <iostream>
#include <math.h>
using namespace std;

// 梯度下降法-常以python实现

// x^0.5 = e^0.5(lnx)
class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) {
            return 0;
        }
        int ans = exp(0.5 * log(x));
        return ((long long)(ans + 1) * (ans + 1) <= x ? ans + 1 : ans); // note: due to the precision of float, you have to check ans with ans+1
    }
};

// 二分查找
class Solution {
public:
    int mySqrt(int x) {
        int l = 0, r = x, ans = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2; // note: search in [l, r)
            if ((long long)mid * mid <= x) {
                ans = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return ans;
    }
};

// 牛顿迭代法--快速求零点
class Solution {
public:
    int mySqrt(int x) {
        // note: 牛顿迭代法无法处理<=0
        if (x == 0) {
            return 0;
        }

        double C = x, x0 = x;
        while (true) {
            double xi = 0.5 * (x0 + C / x0);
            if (fabs(x0 - xi) < 1e-7) {
                break;
            }
            x0 = xi;
        }
        return int(x0);
    }
};

int main()
{
    int x = 4;
    Solution s;
    cout<<s.mySqrt(x)<<endl;
    return 0;
}
