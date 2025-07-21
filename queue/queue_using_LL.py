class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self,front=None,rear=None):
        self.front = front
        self.rear = rear
        self.item_count = 0

    def is_empty(self):
        return self.front == None
    
    def enqueue(self,data):
        n = Node(data)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n
        self.item_count+=1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        elif self.rear == self.front:
            self.rear = None
            self.front = None
        else:
            self.front = self.front.next
        self.item_count-=1

    def get_front(self):
        if not self.is_empty():
            return self.front.item
        raise IndexError("Queue is empty")
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        raise IndexError("Queue is empty")
    
    def size(self):
        return self.item_count
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.size())
print(q.get_front())
print(q.get_rear())
q.dequeue()
print(q.size())
print(q.get_front())