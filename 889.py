from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructFromPrePost(preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    postMap = {x: i for i, x in enumerate(postorder)}

    def dfs(preLeft, preRight, postLeft, postRight):
        if preLeft > preRight:
            return None
        leftCount = 0
        if preLeft < preRight:
            leftCount = postMap[preorder[preLeft + 1]] - postLeft + 1
        return TreeNode(preorder[preLeft],
                        dfs(preLeft + 1, preLeft + leftCount, postLeft, postLeft + leftCount - 1),
                        dfs(preLeft + leftCount + 1, preRight, postLeft + leftCount, postRight - 1))

    return dfs(0, len(preorder) - 1, 0, len(postorder) - 1)
