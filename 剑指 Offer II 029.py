class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def insert(head: 'Node', insertVal: int) -> 'Node':
    TempNode = Node(insertVal)
    if head is None:
        TempNode.next = TempNode
        return TempNode
    if head.next == head:
        head.next = TempNode
        TempNode.next = head
        return head
    curr = head
    P = head.next
    while P != head:
        if curr.val <= insertVal <= P.val:
            break
        if curr.val > P.val:
            if insertVal > curr.val or insertVal < P.val:
                break
        P = P.next
        curr = curr.next
    curr.next = TempNode
    TempNode.next = P
    return head
