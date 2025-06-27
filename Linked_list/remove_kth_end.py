class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
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
    def print(elements):
        temp = head
        while temp is not None:
            print(temp.data,end = "")
            temp = temp.next
        return None

    def removeKthNode(head, k):
        dummy = Node(0)
        dummy.next = head
        first_pointer = dummy
        second_pointer = dummy
        for i in range(k):
            second_pointer = second_pointer.next
        while second_pointer.next!=None:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        first_pointer.next = first_pointer.next.next
        return dummy.next
    
    
arr = [1,2,3,4,5]
my_list = Node
head = my_list.create(arr)
elements = my_list.removeKthNode(head,2)
my_list.print(elements)
    
