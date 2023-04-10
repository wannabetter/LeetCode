from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nextLargerNodes(head: Optional[ListNode]) -> List[int]:
    res = []
    queue = []
    while head:
        while queue and res[queue[-1]] < head.val:
            res[queue.pop()] = head.val
        queue.append(len(res))
        res.append(head.val)
        head = head.next
    while queue:
        res[queue.pop()] = 0
    return res
