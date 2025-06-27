class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self,num):
        self.stack1.append(num)
        return True
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else -1
Q = Queue()
print(Q.enqueue(2))
print(Q.enqueue(3))
print(Q.dequeue())
