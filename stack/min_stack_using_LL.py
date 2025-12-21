class Node:
    def __init__(self,val,min_val,next=None):
        self.val = val
        self.min_val = min_val
        self.next = next

class MinStack:
    def __init__(self):
        self.top = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0
    
    def push(self,value):
        if self.top is None:
            self.top = Node(value,value)
        else:
            current_min = min(value,self.top.min_val)
            self.top = Node(value,current_min,self.top)
        self.item_count+=1

    def pop(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        popped_element = self.top.val
        self.top = self.top.next
        self.item_count-=1
        return popped_element
    
    def peek(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        return self.top.val
    
    def getMin(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        return self.top.min_val
    
    def size(self):
        return self.item_count
    
s = MinStack()
s.push(5)
s.push(3)
s.pop()
print(s.getMin())
print(s.size())
s.push(12)    
print(s.peek())
    
