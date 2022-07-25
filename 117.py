# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: Node) -> Node:
    if root is None:
        return root
    Queue = [root]
    while Queue:
        Temp = Queue
        Queue = []
        while Temp:
            TempNode = Temp.pop(0)
            if TempNode.left:
                Queue.append(TempNode.left)
            if TempNode.right:
                Queue.append(TempNode.right)
            if Temp:
                TempNode.next = Temp[0]
            else:
                TempNode.next = None
    return root
