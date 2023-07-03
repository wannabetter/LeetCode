from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    stack1, stack2 = [], []
    while l1:
        ptr = l1
        l1 = l1.next
        ptr.next = None

        stack1.append(ptr)

    while l2:
        ptr = l2
        l2 = l2.next
        ptr.next = None

        stack1.append(ptr)

    c = 0
    head = ListNode(-1, None)
    while stack1 and stack2:
        val1, val2 = stack1[-1].val, stack2[-1].val
        node = ListNode((val1 + val2 + c) % 10, head.next)

        if val1 + val2 + c > 9:
            c = 1
        else:
            c = 0

        head.next = node
        stack1.pop()
        stack2.pop()

    while stack1:
        val1 = stack1[-1].val
        node = ListNode((val1 + 0 + c) % 10, head.next)

        if val1 + 0 + c > 9:
            c = 1
        else:
            c = 0

        head.next = node
        stack1.pop()

    while stack2:
        val2 = stack2[-1].val
        node = ListNode((val2 + 0 + c) % 10, head.next)

        if val2 + 0 + c > 9:
            c = 1
        else:
            c = 0

        head.next = node
        stack2.pop()

    return head.next