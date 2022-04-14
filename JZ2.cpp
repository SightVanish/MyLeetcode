/*
 * @Author: your name
 * @Date: 2021-09-11 22:12:38
 * @LastEditTime: 2021-09-11 22:53:18
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/.vscode/JZ2.cpp
 */
#include<iostream>
#include<vector>
#include<typeinfo>
#include <algorithm>
using namespace std;

class Solution {
public:

    string replaceSpace(string s) {
        // write code here
        string ans;
        for(int i=0;i<s.size();i++)
        {
            if (s[i]==' ')  s.replace(i, 1, "%20");
        }
        return s;
    }
};

int main()
{
    vector<int> a = {1,2,3,4,5};
    vector<int> b(a.begin(),a.begin()+1);
    for (auto i : b)
    {
        cout << i << endl;
    }

    return 0;
}