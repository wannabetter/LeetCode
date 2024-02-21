from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    def run(left, right):
        if left > right:
            return None
        val = postorder.pop()
        root = TreeNode(val)

        index = maps[val]

        root.right = run(index + 1, right)
        root.left = run(left, index - 1)

        return root

    maps = {val: index for index, val in enumerate(inorder)}
    return run(0, len(inorder) - 1)
