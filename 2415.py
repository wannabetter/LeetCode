class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def reverseOddLevels(root: Optional[TreeNode]) -> Optional[TreeNode]:
    q = [root]
    isOdd = False
    while len(q) > 0:
        if isOdd:
            for i in range(len(q) // 2):
                nodex, nodey = q[i], q[len(q) - 1 - i]
                nodex.val, nodey.val = nodey.val, nodex.val
        tmp = q
        q = []
        for node in tmp:
            if node.left is not None:
                q.append(node.left)
                q.append(node.right)
        isOdd ^= True
    return root
