from collections import Counter
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findDuplicateSubtrees(root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    Res = []
    Cnt = Counter()
    Temp = dict()

    def DFS(Node):
        if not Node:
            return ""
        Chars = str(Node.val) + "(" + DFS(Node.left) + ")" + "(" + DFS(Node.right) + ")"
        Cnt[Chars] += 1
        Temp[Chars] = Node

    for cnt in Cnt:
        if Cnt[cnt] > 1:
            Res.append(Temp[cnt])

    return Res
