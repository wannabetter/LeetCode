from typing import Optional
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob(root: Optional[TreeNode]) -> int:
    f, g = Counter(), Counter()

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        f[node] = node.val + g[node.left] + g[node.right]
        g[node] = max(f[node.left], g[node.left]) + max(f[node.right], g[node.right])

    dfs(root)
    return max(f[root], g[root])
