/*
 * @Author: your name
 * @Date: 2021-09-12 14:18:28
 * @LastEditTime: 2021-09-12 14:51:54
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ11.cpp
 */
#include<iostream>
#include<vector>
#include<typeinfo>
#include <algorithm>
using namespace std;

class Solution {
public:
     int  NumberOf1(int n) {
         int count = 0;
         while(n)
         {
             count++;
             n = n&(n-1);
             // n && n-1 可以保证二进制中的从右往左的第一个1被替换为0，而此左侧的位不受影响
         }

         
         return count;
     }
};
int main()
{
    int n;
    cin>>n;
    vector<int> b;
    while(n)
    {
        b.push_back(n%2);
        n/=2;
    }
    reverse(b.begin(), b.end());
    for(auto i:b)
    {
        cout<<i;
    }
    cout<<endl;
}