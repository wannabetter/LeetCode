from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    head.next = removeNodes(head.next)
    if head.next is not None and head.val < head.next.val:
        return head.next
    else:
        return head