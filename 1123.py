from typing import Optional
from heapq import heappush, heappop


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lcaDeepestLeaves(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(node):
        if not node:
            return 0, None
        left, lcd = dfs(node.left)
        right, rcd = dfs(node.right)
        if left > right:
            return left + 1, lcd
        elif right > left:
            return right + 1, rcd
        else:
            return left + 1, node
    return dfs(root)[-1]