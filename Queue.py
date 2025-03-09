class Queue:
    def __init__(self):
        self.queue = list()
    
    def enque(self, data):
        self.queue.append(data)

    def deque(self):
        if len(self.queue) > 0:
           return self.queue.pop(0)
        else:
            return None
    
    def __str__(self):
        return str(self.queue)
    
MyQueue = Queue()
MyQueue.enque(1)
print(MyQueue)
MyQueue.enque(2)
print(MyQueue)
MyQueue.deque()
print(MyQueue)