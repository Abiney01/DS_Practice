import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Linked_list.linkList import Linked_List

class Stack:
    def __init__(self):
        self.my_list = Linked_List()
        self.item_count = 0

    def is_empty(self):
        return self.my_list.isEmpty()

    def push(self,data):
        self.my_list.insert_at_start(data)
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            data = self.my_list.start.item
            self.my_list.delete_first()
            self.item_count-=1
            return data
        raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.my_list.start.item
        raise IndexError("Stack is empty")
        
    def size(self):
        return self.item_count
    
s = Stack()
s.push(10)
s.push(20)
print(s.peek())
print(s.pop())
print(s.size())
