class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def run(node, target):
        path = list()
        while node != target:
            path.append(node)
            if target.val < node.val:
                node = node.left
            else:
                node = node.right
        path.append(node)
        return path

    path_P = run(root, p)
    path_Q = run(root, q)
    ans = None

    for u, v in zip(path_P, path_Q):
        if u == v:
            ans = u
        else:
            break

    return ans
