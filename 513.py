from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findBottomLeftValue(root: Optional[TreeNode]) -> int:
    Queue = [root]
    ans = root.val
    while len(Queue) != 0:
        P = Queue.pop(0)
        if P.right:  # 必须先放右边，这个顺序是不可以改变的，改变了顺序，遍历出来的最后一个节点就不是最左子节点了
            Queue.append(P.right)
        if P.left:
            Queue.append(P.left)
        ans = P.val
    return ans
