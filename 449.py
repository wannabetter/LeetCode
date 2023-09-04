from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        arr = []

        def postorder(node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            arr.append(node.val)

        postorder(root)
        return " ".join(map(str, arr))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        arr = list(map(int, data.split()))

        def construct(lower, upper):
            if arr == [] or arr[-1] < lower or arr[-1] > upper:
                return None
            val = arr.pop()
            node = TreeNode(val)
            node.right = construct(val, upper)
            node.left = construct(lower, val)
            return node

        return construct(-inf, inf)