from math import inf
from typing import List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    Res = ResTemp = ListNode()
    Index = [node for node in lists]
    Flag = [False if node is not None else True for node in lists]
    while False in Flag:
        Temp = ListNode(10 ** 4 + 1, None)
        MinIndex = -1
        for index, node in enumerate(Index):
            if Flag[index] is False and node.val < Temp.val:
                Temp.val = node.val
                MinIndex = index
        ResTemp.next = Temp
        ResTemp = ResTemp.next
        if Index[MinIndex].next is None:
            Flag[MinIndex] = True
        else:
            Index[MinIndex] = Index[MinIndex].next

    return Res


if __name__ == "__main__":
    lists = [1, 3, 4, 6, 8, 9, 12], [1, 2, 5, 7, 11, 21, 24], [-4, 0, 4, 7, 10, 14, 22, 29]
    head = []
    for pq in lists:
        Temp = TT = ListNode(0, None)
        for p in pq:
            TT.next = ListNode(p, None)
            TT = TT.next
        head.append(Temp)
    print(mergeKLists(head))
