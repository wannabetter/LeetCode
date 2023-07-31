from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: Optional[ListNode]) -> ListNode:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def reverseList(head: Optional[ListNode]) -> ListNode:
    pre = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre


def reorderList(head: Optional[ListNode]) -> None:
    mid = middleNode(head)
    head2 = reverseList(mid)
    while head2.next:
        nxt = head.next
        nxt2 = head2.next
        head.next = head2
        head2.next = nxt
        head = nxt
        head2 = nxt2
