from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertGreatestCommonDivisors(head: Optional[ListNode]) -> Optional[ListNode]:
    def func1(int1,int2):
        m = max(int1, int2)
        n = min(int1, int2)
        r = m % n
        while r != 0:
            m = n
            n = r
            r = m % n
        return n

    prev, cur = head, head.next
    if not cur:
        return head
    while prev.next:
        pos = prev
        prev = cur

        node = ListNode(func1(pos.val,cur.val),cur)
        pos.next = node

        cur = cur.next
    return head

