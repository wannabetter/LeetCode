from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root: 'Node') -> List[int]:
    ans = []

    def run(node):
        if not node:
            return
        ans.append(node.val)
        for kid in node.children:
            run(kid)

    run(root)
    return ans
