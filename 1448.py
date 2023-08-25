class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root: TreeNode) -> int:
    def DFS(node, max_val):
        ans = 0
        if not node:
            return ans
        if node.val >= max_val:
            ans = ans + 1
            max_val = node.val
        ans += DFS(node.left, max_val)
        ans += DFS(node.right, max_val)
        return ans

    return DFS(root, root.val)
