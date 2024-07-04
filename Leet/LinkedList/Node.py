class ListNode:
    def __init__(self,val = 0) -> None:
        self.value = val
        self.next = None
    
def createNewNode(val):
    return ListNode(val  = val)
    