from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def reverseOddLevels(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def DFS(Left, Right, High):
        if not Left:
            return
        if High % 2 != 0:
            Left.val, Right.val = Right.val, Left.val
        DFS(Left.left, Right.right, High + 1)
        DFS(Left.right, Right.left, High + 1)

    DFS(root.left, root.right, 1)
    return root
