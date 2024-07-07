from Node import ListNode

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)


def printNode(head):
    ptr = head
    while ptr:
        print(ptr.value)
        ptr = ptr.next

def insertionSortLinkedList(head):
    if head is None or head.next is None:
        return head

    dummy = ListNode(0)
    dummy.next = head
    current = head
    while current and current.next:
        if current.value <= current.next.value:
            current = current.next
        else:
            insert = current.next
            current.next = insert.next
            prev = dummy
            while prev.next and prev.next.value < insert.value:
                prev = prev.next
            
            insert.next = prev.next
            prev.next = insert
    
    return dummy.next


printNode(insertionSortLinkedList(head=head))