from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delNodes(root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    ans = []
    to_delete_set = set(to_delete)

    def DFS(node, is_root, to_delete_set):
        if not node:
            return
        delete = node.val in to_delete_set
        node.left=DFS(node.left,delete,to_delete_set)
        node.right=DFS(node.right,delete,to_delete_set)

        if delete:
            return
        else:
            if is_root:
                ans.append(node)
            else:
                return node

    DFS(root,True,to_delete_set)
    return ans
