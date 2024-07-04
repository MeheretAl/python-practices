from collections import defaultdict
import Node

def nextLargerNodes(head: Node.ListNode) -> list[int]:
        freq = defaultdict(int)
        ptr = head
        ans = []
        currMax = 0
        #find the maxmimum for the first iteration
        while ptr:
            currMax = max(ptr.value,currMax)
            freq[ptr.value]+=1
            ptr = ptr.next
        
        ptr = head
        while ptr:
            currVal = ptr.value
            if freq[currMax] > 0 and ptr.value < currMax:
                
                ans.append(currMax)
                freq[ptr.value] -= 1
            elif freq[ptr.value] > 0 and ptr.value == currMax:
                ans.append(0)
                freq[ptr.value] -= 1
            
            if freq[currMax] == 0:
                del freq[currMax]
                currMax = max(freq)
            else:
                freq[currMax] -= 1
            

            ptr = ptr.next
        
        return ans

head = Node.ListNode(2)
head.next = Node.createNewNode(7)
head.next.next = Node.createNewNode(4)
head.next.next.next = Node.createNewNode(3)
head.next.next.next.next = Node.createNewNode(5)

print(nextLargerNodes(head=head))
