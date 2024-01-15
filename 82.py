from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(val=-1, next=head)
    prev, cur = dummy, dummy.next
    while cur and cur.next:
        if cur.val == cur.next.val:
            val = cur.val
            while cur and val == cur.val:
                cur = cur.next
            prev.next = cur
        else:
            cur = cur.next
            prev = prev.next
    return dummy.next




