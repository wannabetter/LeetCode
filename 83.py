from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    node_set = set([head.val])
    prev, cur = head, head.next
    while cur:
        if cur.val not in node_set:
            node_set.add(cur.val)
            cur = cur.next
            prev = prev.next
        else:
            cur = cur.next
            prev.next = cur
    return head
