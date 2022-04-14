/*
 * @Author: your name
 * @Date: 2021-09-11 23:04:01
 * @LastEditTime: 2021-09-11 23:04:01
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ4.cpp
 */

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        if (pre.size()==0)    return nullptr;
        TreeNode* head = new TreeNode(pre[0]); // create the head node
        int i = 0;
        while(vin[i]!=pre[0])    i++;
        // i is the index of root
        vector<int> left_pre (pre.begin()+1,pre.begin()+i+1);
        vector<int> left_vin (vin.begin(),vin.begin()+i);
        vector<int> right_pre (pre.begin()+i+1,pre.end());
        vector<int> right_vin (vin.begin()+i+1,vin.end());
        
        head->left = reConstructBinaryTree(left_pre, left_vin);
        head->right = reConstructBinaryTree(right_pre, right_vin);
        return head;
    }
};