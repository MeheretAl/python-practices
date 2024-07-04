import Node
        
def splitNodesToParts(head:Node.ListNode,k:int) -> list[Node.ListNode]:
    ans = []
    ptr = head
    counter = 0
    while ptr:
        counter += 1
        ptr = ptr.next
    if k >= counter:
        counter = 0
        ptr = head
        while counter < k:
            part = []
            if not ptr:
                part.append(None)
            else:
                curr = ptr 
                ptr = ptr.next
                curr.next = None
                part.append(curr.value)

            ans.append(part)
            counter += 1
        
    return ans

head = Node.ListNode(1)
head.next = Node.createNewNode(2)
head.next.next = Node.createNewNode(3)

print(splitNodesToParts(head,5))


