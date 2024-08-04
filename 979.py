from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def distributeCoins(root: Optional[TreeNode]) -> int:
    ans = 0

    def DFS(node):
        nonlocal ans
        left, right = 0, 0
        if node is None:
            return 0
        if node.left is not None:
            left = DFS(node.left)
        if node.right is not None:
            right = DFS(node.right)
        ans += abs(left) + abs(right)
        return left + right + node.val - 1

    DFS(root)
    return ans
