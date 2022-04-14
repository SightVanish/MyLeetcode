/*
 * @Author: your name
 * @Date: 2021-09-12 17:07:11
 * @LastEditTime: 2021-09-12 19:00:06
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ17.cpp
 */

/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/

class Solution {
public:
    bool isSubtree(TreeNode* p1, TreeNode* p2)
    {
        if (p2==nullptr)    return true;
        else if (p1==nullptr)    return false;
        
        return p1->val==p2->val && isSubtree(p1->left,p2->left) && isSubtree(p1->right,p2->right);
    }
    bool HasSubtree(TreeNode* p1, TreeNode* p2)
    {
        if (p1==nullptr || p2==nullptr)    return false; // 此时为子结构
        // 若是考虑为子树，则当p1，p2同为null时，return true
        return isSubtree(p1,p2) || HasSubtree(p1->left,p2) || HasSubtree(p1->right,p2);
    }
};