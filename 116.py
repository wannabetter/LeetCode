from typing import Optional


class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root: Optional[Node]) -> Optional[Node]:
    if not root:
        return root
    Queue = [root]
    while Queue:
        Temp = Queue
        Queue = []
        while Temp:
            cur = Temp.pop(0)
            if cur.left:
                Queue.append(cur.left)
            if cur.right:
                Queue.append(cur.right)
            if Temp:
                cur.next = Temp[0]
            else:
                cur.next = None
    return root