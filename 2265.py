from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfSubtree(root: Optional[TreeNode]) -> int:
    Sum = 0

    def DFS(Node):
        nonlocal Sum
        if not Node:
            return 0, 0
        LeftN, LeftS = DFS(Node.left)
        RightN, RightS = DFS(Node.right)
        NodeSum = LeftS + Node.val + RightS
        NodeNum = LeftN + RightN + 1
        if NodeSum // NodeNum == Node.val:
            Sum += 1
        return NodeNum, NodeSum

    DFS(root)
    return Sum
