/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/

// 简单算法--先中序遍历，再根据遍历结果调整
class Solution {
public:
    TreeNode* Convert(TreeNode* pRootOfTree) 
    {
        vector<TreeNode*> path;
        inorder(pRootOfTree, path);
        for (int i=0; i<path.size(); i++)
        {
            if (i==0)
            {
                path[i]->left=nullptr;
                path[i]->right=path[i+1];
            }
            else if(i==(path.size()-1))
            {
                path[i]->left=path[i-1];
                path[i]->right=nullptr;
            }
            else
            {
                path[i]->left=path[i-1];
                path[i]->right=path[i+1];
            }
        }
        return path[0];
    }
    void inorder(TreeNode* root, vector<TreeNode*>& path)
    {
        if (root==nullptr)    return;
        inorder(root->left, path);
        path.push_back(root);
        inorder(root->right, path);
    }
};