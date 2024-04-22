class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

def sortList(self, head:ListNode):
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    mid = slow.next
    slow.next = None

    left = self.sortList(head)
    right = self.sortList(mid)

    dummy = ListNode(0)
    curr = dummy
    while left != None and right != None:
        if left.val <= right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next

    if left:
        curr.next = left
    if right:
        curr.next = right

    return dummy.next