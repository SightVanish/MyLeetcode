/*
 * @Author: your name
 * @Date: 2021-09-12 17:07:34
 * @LastEditTime: 2021-09-12 21:02:08
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ23.cpp
 */
class Solution {
public:
    bool VerifySquenceOfBST(vector<int> sequence) {
        if (sequence.size()==0)    return false;
        return check(sequence, 0, sequence.size()-1);
    }
    bool check(vector<int>& sequence, int l, int r)
    {
        if (l>=r)    return true; // there is only one element
        int root=sequence[r];
        int i = l-1; // note: it should be l-1, otherwise it cannot handle the situation that there is no left part tree
        while(sequence[i]<root && i<r-1)
        {
            i++;
        }
        for(int j=i+1;j<r;j++)
        {
            if (sequence[j]<root)    return false;
        }
        return check(sequence, l, i) && check(sequence, i+1, r-1);
    }
};