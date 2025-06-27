class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def peek(self):
        if not self.is_empty:
            return self.items[-1]
        raise IndexError("Stack is empty")
    def pop(self):
        if not self.is_empty:
            return self.items.pop()
        raise IndexError("Stack is empty")
    def size(self):
        return len(self.items)
    