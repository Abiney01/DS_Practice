class Queue:
    def __init__(self):
        self.my_list = []

    def is_empty(self):
        return len(self.my_list) == 0
    
    def enqueue(self,data):
        self.my_list.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.my_list.pop(0)
        raise IndexError("Queue is empty")

    def get_front(self):
        if not self.is_empty():
            return self.my_list[0]
        raise IndexError("Queue is empty")
    
    def get_rear(self):
        if not self.is_empty():
            return self.my_list[-1]
        raise IndexError("Queue is empty")
    
    def size(self):
        return len(self.my_list)
    
q = Queue()
print(q.size())
try:
    print(q.get_front())
except IndexError as e:
    print(e)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.size())
print(q.get_front())
print(q.get_rear())
q.dequeue()
print(q.size())