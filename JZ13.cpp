/*
 * @Author: your name
 * @Date: 2021-09-12 15:12:49
 * @LastEditTime: 2021-09-12 15:20:44
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ13.cpp
 */
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param array int整型vector 
     * @return int整型vector
     */
    vector<int> reOrderArray(vector<int>& array) {
        // write code here
        vector<int> odd;
        vector<int> even;
        for (auto i: array)
        {
            if(i%2)    odd.push_back(i);
            else    even.push_back(i);
        }

        odd.insert(odd.end(), even.begin(), even.end());
        return odd;
    }
};