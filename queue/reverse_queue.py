from queue import Queue

def reverse_queue(q):
    stack = []

    # Step 1: Transfer elements from queue to stack
    while not q.empty():
        stack.append(q.get())  # Dequeue operation

    # Step 2: Transfer elements back from stack to queue
    while stack:
        q.put(stack.pop())  # Enqueue operation

def process_test_cases():
    T = int(input())  # Number of test cases
    
    for _ in range(T):
        N = int(input())  # Number of elements in queue
        elements = list(map(int, input().split()))  # Read elements
        
        q = Queue()  # Create a queue
        for ele in elements:
            q.put(ele)  # Enqueue elements

        reverse_queue(q)  # Reverse the queue

        # Print reversed queue elements
        while not q.empty():
            print(q.get(), end=" ")
        print()  # Newline for the next test case

# Run the function to process input
process_test_cases()
