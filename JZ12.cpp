/*
 * @Author: your name
 * @Date: 2021-09-12 14:51:59
 * @LastEditTime: 2021-09-12 15:12:41
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ12.cpp
 */

class Solution {
public:
    double Power(double base, int exponent) {
        int n = abs(exponent);
        if (exponent<0)
        {
            exponent = -exponent;
            base = 1/base;
        }
        
        double ans = 1.0;
        while(n)
        {
            if(n&1)
            {
                ans*=base;
            }
            base*=base;
            n>>=1;
        }

        return ans;
    }
};