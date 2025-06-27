from typing import *
def next_greater_element(arr, n):
    stack = []
    result = [-1] * n  # Initialize result with -1

    for i in range(n - 1, -1, -1):  # Traverse from right to left
        while stack and stack[-1] <= arr[i]:  
            stack.pop()  # Remove smaller elements

        if stack:
            result[i] = stack[-1]  # Set the next greater element
        
        stack.append(arr[i])  # Push current element to stack
    
    return result

# Read input
t = int(input().strip())  # Number of test cases
for _ in range(t):
    n = int(input().strip())  # Length of array
    arr = list(map(int, input().strip().split()))
    print(*next_greater_element(arr, n))


# method2(leetcode)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nge_map = {}
        for i in reversed(nums2):
            while stack and stack[-1] <= i:
                stack.pop()
            nge_map[i] = stack[-1] if stack else -1
            stack.append(i)
        return [nge_map[i] for i in nums1]