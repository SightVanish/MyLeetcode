/*
 * @Author: your name
 * @Date: 2021-09-12 17:07:16
 * @LastEditTime: 2021-09-12 19:02:57
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ18.cpp
 */
/**
 * struct TreeNode {
 *	int val;
 *	struct TreeNode *left;
 *	struct TreeNode *right;
 *	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * };
 */
class Solution {
public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     *
     * 
     * @param pRoot TreeNode类 
     * @return TreeNode类
     */
    TreeNode* Mirror(TreeNode* pRoot) {
        // write code here
        if (pRoot==nullptr)    return nullptr;
        auto p = pRoot->left;
        pRoot->left = pRoot->right;
        pRoot->right = p;
        Mirror(pRoot->left);
        Mirror(pRoot->right);
        return pRoot;
    }
};