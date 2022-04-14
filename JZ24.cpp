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
    vector<vector<int> > FindPath(TreeNode* root,int expectNumber) {
        vector<vector<int>> ret;
        vector<int> path;
        if(!root)    return ret;
        Path(root, ret, path, expectNumber);
        
        sort(ret.begin(), ret.end());
        return ret;
    }
    
    void Path(TreeNode* root, vector<vector<int>>& ret, vector<int>& path, int sum)
    {
        path.push_back(root->val);
        // this is a leaf node
        if(root->val==sum && root->left==nullptr && root->right==nullptr)
        {
            ret.push_back(path);
//             return; // no return here! you have to pop the node
        }
        
        if(root->left)    Path(root->left, ret, path, sum-root->val);
        if(root->right)    Path(root->right, ret, path, sum-root->val);
        path.pop_back(); // 此时path节点被逐层删除，path已经push到ret中，或此回路无效
    }
};