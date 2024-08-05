class Queue:
    def __init__(self):
        self.queue = []
        self.headIdx = 0

    def append(self,value):
        self.queue.append(value)

    def pop(self):
        if self.headIdx < len(self.queue):
            val = self.queue[self.headIdx]
            self.headIdx += 1
            return val
    def is_empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False
    
    def peek(self):
        return self.queue[self.headIdx]

    def size(self):
        return len(self.queue) - self.headIdx
    
    def clear(self):
        self.queue = []
        self.headIdx = 0