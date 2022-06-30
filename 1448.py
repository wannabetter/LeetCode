# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodHelp(self, root: TreeNode, Max: int) -> int:
        if root is None:
            return 0
        ret = 0
        newMax = Max
        if root.val >= newMax:
            ret = ret + 1
            newMax = root.val
        leftVal = self.goodHelp(root.left, newMax)
        rightVal = self.goodHelp(root.right, newMax)
        return leftVal + rightVal + ret

    def goodNodes(self, root: TreeNode) -> int:
        return self.goodHelp(root, root.val)
