class TreeNode:
    def __init__(self, Val, Next):
        self.Val = Val
        self.Next = Next


class MyLinkedList:

    def __init__(self):
        self.Len = 0
        self.Head = TreeNode(None, None)

    def get(self, index: int) -> int:
        if index < self.Len:
            idx = 0
            Node = self.Head.Next
            while idx < index:
                Node = Node.Next
                idx += 1
            return Node.Val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(val, 0)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(val, self.Len)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            newNode = TreeNode(val, self.Head.Next)
            self.Head.Next = newNode
        elif index > self.Len:
            return
        elif index == self.Len:
            Node = self.Head.Next
            while Node.Next:
                Node = Node.Next
            Node.Next = TreeNode(val, None)
        else:
            idx = 0
            Node = self.Head
            while idx < index:
                idx += 1
                Node = Node.Next
            newNode = TreeNode(val, Node.Next)
            Node.Next = newNode
        self.Len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.Len:
            idx = 0
            Node = self.Head
            while idx < index:
                Node = Node.Next
                idx += 1
            Node.Next = Node.Next.Next
            self.Len -= 1
