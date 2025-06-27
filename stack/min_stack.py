class MinStack:
    def __init__(self):
        self.stack = []  # Main stack
        self.min_stack = []  # Stack to store minimum elements

    def push(self, num: int):
        self.stack.append(num)
        # Push onto min_stack if it's empty or num is the new minimum
        if not self.min_stack or num <= self.min_stack[-1]:
            self.min_stack.append(num)

    def pop(self):
        if not self.stack:
            return -1
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        return popped

    def top(self):
        return self.stack[-1] if self.stack else -1

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else -1

# Function to process the input cases
def process_operations(operations):
    stack = MinStack()
    output = []
    
    for op in operations:
        if op[0] == 1:  # Push operation
            stack.push(op[1])
        elif op[0] == 2:  # Pop operation
            output.append(stack.pop())
        elif op[0] == 3:  # Top operation
            output.append(stack.top())
        elif op[0] == 4:  # getMin operation
            output.append(stack.getMin())

    return " ".join(map(str, output))

# Sample Input Processing
def main():
    test_cases = int(input().strip())  # Number of test cases
    results = []
    
    for _ in range(test_cases):
        num_operations = int(input().strip())  # Number of operations
        operations = []
        for _ in range(num_operations):
            ops = list(map(int, input().strip().split()))
            operations.append(ops)
        results.append(process_operations(operations))
    
    # Print all results for test cases
    for res in results:
        print(res)

# Uncomment to run the program
if __name__ == "__main__":
    main()
