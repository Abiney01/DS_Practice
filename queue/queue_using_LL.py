class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.item_count = 0
    # def print(self):
    #     while self.front is not None:
    #         print(self.front.item,end=" ")
    #         self.front = self.front.next
    def is_empty(self):
        return self.rear == None
    def enqueue(self,data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is Underflow")
        elif self.rear == self.front:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("Stack is Underflow")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Stack is Underflow")
        else:
            return self.rear.item
    def get_size(self):
        return self.item_count
Q = Queue()
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
print(Q.get_front())
Q.dequeue()
print(Q.get_front())
Q.enqueue(200)
print(Q.get_rear())
Q.print()



