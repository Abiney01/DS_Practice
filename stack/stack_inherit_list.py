class Stack(list):
    def is_empty(self):
        return len(self) == 0
    
    def push(self,data):
        self.append(data)

    def pop(self):
        return super().pop()
    
    def peek(self):
        return self[-1]
    
    def size(self):
        return len(self)
    
    def insert(self, index, data):
        raise AttributeError("Invalid attribute 'insert' in Stack class")
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())
print(s.pop())
print(s.size())
# s.insert(2,12)