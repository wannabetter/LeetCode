class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    if not root1:
        return root2
    if not root2:
        return root1

    Tree = TreeNode(root1.val + root2.val, left=mergeTrees(root1.left, root2.left),
                    right=mergeTrees(root1.right, root2.right))
    return Tree
