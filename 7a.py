class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return "Stack is empty"

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return "Queue is empty"

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())
