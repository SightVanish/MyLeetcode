/*
 * @Author: your name
 * @Date: 2021-09-12 17:07:19
 * @LastEditTime: 2021-09-12 19:36:36
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ19.cpp
 */
#include<iostream>
#include<vector>
#include<typeinfo>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int> > rotateMatrix(vector<vector<int> > matrix)
    {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int> > res;
        for (int i=0; i<n; i++)
        {
            vector<int> tmp;
            for (int j=0;j<m;j++)
            {
                tmp.push_back(matrix[j][n-1-i]);
            }
            res.push_back(tmp);
        }
        return res;
    }
    vector<int> printMatrix(vector<vector<int> > matrix) {
        vector<int> res;
        while(!matrix.empty())
        {
             for(auto i:matrix[0])
             {
                 res.push_back(i);
             }
            matrix.erase(matrix.begin());
            if (!matrix.empty())    matrix = rotateMatrix(matrix);
        }
       return res;
    }
};