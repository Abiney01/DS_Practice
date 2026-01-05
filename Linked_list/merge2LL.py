class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        output = dummy

        pointer1 = list1
        pointer2 = list2

        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                output.next = pointer1
                pointer1 = pointer1.next
            else:
                output.next = pointer2
                pointer2 = pointer2.next
            output = output.next

        if pointer1:
            output.next = pointer1
        else:
            output.next = pointer2

        return dummy.next

def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

list1 = build_linked_list([1, 3, 5])
list2 = build_linked_list([2, 4, 6])

result = Solution().mergeTwoLists(list1, list2)
print_linked_list(result)