from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def widthOfBinaryTree(root: Optional[TreeNode]) -> int:
    MaxWid = 1
    root.val = 1
    Queue = [root]
    while Queue:
        MaxWid = max(MaxWid, Queue[-1].val - Queue[0].val + 1)
        Temp = Queue
        Queue = []
        while Temp:
            Node = Temp.pop(0)
            if Node.left:
                Node.left.val = Node.val * 2
                Queue.append(Node.left)
            if Node.right:
                Node.right.val = Node.val * 2 + 1
                Queue.append(Node.right)
    return MaxWid
