def stockSpan(prices, n):
    stack = []
    span = [0] * n

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        if not stack:
            span[i] = i + 1
        else:
            span[i] = i - stack[-1]

        stack.append(i)

    return span

# Read input
t = int(input().strip())  # Number of test cases
for _ in range(t):
    n = int(input().strip())  # Number of days
    prices = list(map(int, input().strip().split()))
    result = stockSpan(prices, n)
    print(*result)


# Leetcode
class StockSpanner:

    def __init__(self):
        self.stack = []  # Stack to store (price, span) pairs

    def next(self, price: int) -> int:
        span = 1  # Start with a span of 1 (today itself)
        
        # Pop elements while the stack is not empty and the top price is <= current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]  # Add the span of the popped element
        
        # Push the current price with its span
        self.stack.append((price, span))
        
        return span


# Example usage:
obj = StockSpanner()
print(obj.next(100))  # Output: 1
print(obj.next(80))   # Output: 1
print(obj.next(60))   # Output: 1
print(obj.next(70))   # Output: 2
print(obj.next(60))   # Output: 1
print(obj.next(75))   # Output: 4
print(obj.next(85))   # Output: 6
