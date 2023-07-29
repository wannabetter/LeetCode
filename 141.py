from typing import Optional
from collections import Counter


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    cnt = Counter()
    cur = head
    while cur:
        if cnt[cur] == 0:
            cnt[cur] = 1
        else:
            return True
        cur = cur.next
    return False
