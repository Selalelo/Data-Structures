class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) > 0:
             self.stack.pop()
        else:
            return None
        
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
    
    def count(self):
        if len(self.stack) > 0:
            return len(self.stack)
        else:
            return None
    
    def clear(self):
        if len(self.stack) > 0:
            self.stack.clear()
            return self.stack
    
        
    def __str__(self):
        return str(self.stack)
    

myStack = Stack()
myStack.push(1)
print(myStack)
myStack.push(2)
print(myStack)
print(myStack.count())
print(myStack.clear())
print(myStack)
print(myStack.peek())
myStack.pop()
print(myStack)