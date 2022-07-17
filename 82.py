class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
    if not head:
        return head
    else:
        Dummy = ListNode(0, head)
        Cur = Dummy
        while Cur.next and Cur.next.next:
            if Cur.next.val == Cur.next.next.val:
                Val = Cur.next.val
                while Cur.next and Cur.next.val == Val:
                    Cur.next = Cur.next.next
            else:
                Cur = Cur.next
        return Dummy.next
