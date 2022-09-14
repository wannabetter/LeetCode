from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree2str(root: Optional[TreeNode]) -> str:
    def DFS(Node):
        if Node.left and Node.right:
            return str(Node.val) + "(" + DFS(Node.left) + ")" + "(" + DFS(Node.right) + ")"
        if not Node.left and Node.right:
            return str(Node.val) + "()" + "(" + DFS(Node.right) + ")"
        if Node.left and not Node.right:
            return str(Node.val) + "(" + DFS(Node.left) + ")"
        if not Node.left and not Node.right:
            return str(Node.val)

    return DFS(root)
