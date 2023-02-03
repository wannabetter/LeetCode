from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def btreeGameWinningMove(root: Optional[TreeNode], n: int, x: int) -> bool:
    xNode = None

    def getNode(root):
        if not root:
            return 0
        if root.val == x:
            nonlocal xNode
            xNode = root
        return 1 + getNode(root.left) + getNode(root.right)

    getNode(root)
    lArea, rArea = getNode(xNode.left), getNode(xNode.right)
    arr = sorted([n - lArea - rArea - 1, lArea, rArea])
    return arr[-1] >= (n + 1) // 2