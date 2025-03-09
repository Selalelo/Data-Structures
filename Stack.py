class Stack:
    def __init__(self):
        self.stack = list()
    
    def pop(self):
        if len(self.stack) > 0:
             self.stack.pop()
        else:
            return None
        
    def push(self, data):
        self.stack.append(data)

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
    def __str__(self):
        return str(self.stack)
    

myStack = Stack()
myStack.push(1)
print(myStack)
myStack.push(2)
print(myStack)
print(myStack.peek())
myStack.pop()
print(myStack)