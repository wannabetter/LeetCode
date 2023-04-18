from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxAncestorDiff(root: Optional[TreeNode]) -> int:
    def DFS(curNode, minNum, maxNum):
        if not curNode:
            return maxNum - minNum
        minNum, maxNum = min(minNum, curNode.val), max(maxNum, curNode.val)
        resLeft = DFS(curNode.left, minNum, maxNum)
        resRight = DFS(curNode.right, minNum, maxNum)
        return max(maxNum - minNum, resLeft, resRight)

    return DFS(root, root.val, root.val)
