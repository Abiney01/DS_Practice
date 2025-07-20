import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Linked_list.linkList import Linked_List

class Stack(Linked_List):
    def __init__(self):
        super().__init__()
        self.item_count = 0
    def is_empty(self):
        return super().isEmpty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.delete_first()
            self.item_count-=1
            return data
        raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.start.item
        raise IndexError("Stack is empty")
    
    def size(self):
        return self.item_count
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.size())
print(s.pop())
print(s.peek())

            