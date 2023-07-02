from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    c = 0
    ptr = ptr_head = ListNode(-1, None)
    while l1 and l2:
        node = ListNode((l1.val + l2.val + c) % 10, None)
        if l1.val + l2.val + c > 9:
            c = 1
        else:
            c = 0
        ptr.next = node
        ptr = ptr.next

        l1 = l1.next
        l2 = l2.next

    while l1:
        node = ListNode((l1.val + 0 + c) % 10, None)
        if l1.val + 0 + c > 9:
            c = 1
        else:
            c = 0
        ptr.next = node
        ptr = ptr.next

        l1 = l1.next

    while l2:
        node = ListNode((l2.val + 0 + c) % 10, None)
        if l2.val + 0 + c > 9:
            c = 1
        else:
            c = 0
        ptr.next = node
        ptr = ptr.next

        l2 = l2.next

    if c == 1:
        node = ListNode(1, None)
        ptr.next = node

    return ptr_head.next
