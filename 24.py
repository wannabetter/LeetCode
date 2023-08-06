from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    rear = dummy = ListNode(-1, None)
    if not (head and head.next):
        return head
    while head and head.next:
        cur = head.next.next
        p1, p2 = head, head.next
        p1.next, p2.next = None, None
        rear.next = p2
        rear = p2
        rear.next = p1
        rear = p1
        head = cur
    if head:
        rear.next = head
    return dummy.next