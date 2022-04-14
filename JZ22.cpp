/*
 * @Author: your name
 * @Date: 2021-09-12 17:07:30
 * @LastEditTime: 2021-09-12 20:12:12
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /剑指offer/JZ22.cpp
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
    vector<int> PrintFromTopToBottom(TreeNode* root) {
        vector<int> res;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty())
        {
            auto top = q.front();
            if(top==nullptr)
            {
                q.pop();
                continue;
            }
            q.push(top->left);
            q.push(top->right);
            
            res.push_back(top->val);
            q.pop();
        }
        return res;
    }
};