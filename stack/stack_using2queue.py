class StackUsingQueues:
    def __init__(self):
        self.q1 = []  # Main queue
        self.q2 = []  # Temporary queue

    def push(self, data: int):
        # Push data into q2
        self.q2.append(data)
        # Transfer all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.pop(0))
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        if not self.q1:
            return -1
        return self.q1.pop(0)

    def top(self) -> int:
        if not self.q1:
            return -1
        return self.q1[0]

    def size(self) -> int:
        return len(self.q1)

    def isEmpty(self) -> bool:
        return len(self.q1) == 0

# Handling queries
def process_queries(queries):
    stack = StackUsingQueues()
    for query in queries:
        if query[0] == 1:
            stack.push(query[1])
        elif query[0] == 2:
            print(stack.pop())
        elif query[0] == 3:
            print(stack.top())
        elif query[0] == 4:
            print(stack.size())
        elif query[0] == 5:
            print("true" if stack.isEmpty() else "false")

# Example test case
queries = [
    [1, 13],
    [1, 47],
    [4],
    [5],
    [2],
    [3]
]
process_queries(queries)
