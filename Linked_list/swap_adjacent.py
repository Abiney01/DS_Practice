class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    @staticmethod
    def swapPairs(head):
        dummy = ListNode(0)
        dummy.next = head
        point = dummy
        while point.next is not None and point.next.next is not None:
            swap1 = point.next
            swap2 = point.next.next
            swap1.next = swap2.next
            swap2.next = swap1
            point.next = swap2
            point = swap1
        return dummy.next
    @staticmethod
    def create(arr):
        if arr is None:
            return None
        head = ListNode(arr[0])
        temp = head
        for value in arr[1:]:
            # if value ==-1:
            #     break
            temp.next = ListNode(value)
            temp = temp.next
        return head
    @staticmethod
    def print(elements):
        temp = elements
        while temp is not None:
            print(temp.val,end = "")
            temp = temp.next
        return None
arr = [1,2,3,4]
my_list = ListNode
head = my_list.create(arr)
elements = my_list.swapPairs(head)
my_list.print(elements)

