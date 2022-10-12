from typing import Optional
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def numComponents(head: Optional[ListNode], nums: List[int]) -> int:
    P = head
    Sum = 0
    while P:
        if P.val in nums:
            while P and P.val in nums:
                P = P.next
            Sum += 1
        else:
            P = P.next
    return Sum
