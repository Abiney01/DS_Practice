class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertionSortList(head):
    if not head or not head.next:
        return head

    dummy = ListNode(0)  # Dummy node to simplify insertion logic
    current = head

    while current:
        prev = dummy  # Start at the beginning of the sorted list
        next_node = current.next  # Store the next node
        # print(prev.next,prev.val,current.val)
        # print(prev,"curprev",current)
        # print(prev.next,"prevnext")

        # Find the correct position in the sorted list
        while prev.next and prev.next.val < current.val:
            # print(prev,prev.next,"vsa",prev.next.val,current.val)
            prev = prev.next
 
        # Insert current node
        current.next = prev.next
        prev.next = current

        current = next_node  # Move to the next node in the input list

    return dummy.next  # Return the sorted list

def printList(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" ".join(result))

def createLinkedList(arr):
    if not arr or arr[0] == -1:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        if val == -1:
            break
        current.next = ListNode(val)
        current = current.next
    return head


arr = [3,4,1,2,5]
head = createLinkedList(arr)
sorted_head = insertionSortList(head)
# printList(sorted_head)
