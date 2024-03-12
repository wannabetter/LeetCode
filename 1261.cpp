//
// Created by DELL on 2024/3/12.
//

#include <set>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class FindElements {
public:

    void TreeInit(TreeNode *node, int val) {
        node->val == val;
        cnt.insert(val);
        if (node->left != nullptr) {
            TreeInit(node->left, val * 2 + 1);
        }
        if (node->right != nullptr) {
            TreeInit(node->right, val * 2 + 2);
        }
    }

    FindElements(TreeNode *root) {
        TreeInit(root, 0);
    }

    bool find(int target) {
        return cnt.find(target) != cnt.end();
    }

private:
    set<int> cnt;
};

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements* obj = new FindElements(root);
 * bool param_1 = obj->find(target);
 */