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
    def findMiddle(head):
        slow = head
        fast = head
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow.data


arr = [1,2,3,4,5]
my_list = Node
head = my_list.create(arr)
print(my_list.findMiddle(head))