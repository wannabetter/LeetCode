class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bstToGst(root: TreeNode) -> TreeNode:
    def run(root: TreeNode):
        nonlocal total
        if root:
            run(root.right)
            total += root.val
            root.val = total
            run(root.left)
    total = 0
    run(root)
    return root
