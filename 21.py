from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    P = head = ListNode()
    while list1 and list2:
        if list1.val <= list2.val:
            Temp = ListNode(list1.val, None)
            P.next = Temp
            P = Temp
            list1 = list1.next
        else:
            Temp = ListNode(list2.val, None)
            P.next = Temp
            P = Temp
            list2 = list2.next

    while list1:
        Temp = ListNode(list1.val, None)
        P.next = Temp
        P = Temp
        list1 = list1.next

    while list2:
        Temp = ListNode(list2.val, None)
        P.next = Temp
        P = Temp
        list2 = list2.next

    return head.next