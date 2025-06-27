class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def reverse(head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev 
            prev = current
            current = next_node
        return prev 
    def print(head):
        temp = head
        while temp:
            print(temp.data,end =' ')
            temp = temp.next
        # print("-1")
    def create(arr):
        if arr is None:
            return None
        head = Node(arr[0])
        temp = head
        for value in arr[1:]:
            # if value ==-1:
            #     break
            temp.next = Node(value)
            temp = temp.next
        return head


arr = [1,2,3,4,5]
my_list = Node
head = my_list.create(arr)
reverse = my_list.reverse(head)
my_list.print(reverse)

# from collections import deque

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

#     @staticmethod
#     def create(arr):
#         if not arr or arr[0] == -1:
#             return None
#         head = Node(arr[0])
#         temp = head
#         for value in arr[1:]:
#             if value == -1:
#                 break
#             temp.next = Node(value)
#             temp = temp.next
#         return head

#     @staticmethod
#     def reverse(head):
#         if not head:
#             return None
        
#         # Use deque to store nodes
#         stack = deque()
#         current = head
#         while current:
#             stack.append(current)
#             current = current.next
        
#         # Pop from stack to reverse order
#         new_head = stack.pop()
#         temp = new_head
#         while stack:
#             temp.next = stack.pop()
#             temp = temp.next
        
#         temp.next = None  # Last node should point to None
#         return new_head

#     @staticmethod
#     def print(head):
#         temp = head
#         while temp:
#             print(temp.data, end=" ")
#             temp = temp.next
#         print("-1")  # End with "-1" as per the problem statement

# # Test Case
# arr = [1, 2, 3, 4, 5, -1]
# head = Node.create(arr)
# reversed_head = Node.reverse(head)
# Node.print(reversed_head)
