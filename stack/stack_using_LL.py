class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class Stack:
    def __init__(self):
        self.start = None
        self.item_count = 0
    def is_empty(self):
        return self.start==None
    def push(self,item):
        n = Node(item,self.start)
        self.start = n 
        self.item_count+=1
    def pop(self,item):
        if not self.is_empty:
            temp = self.start.item
            self.start = self.start.next
            self.item_count-=1
            return temp
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty:
            return self.start.item
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return self.item_count
    
        