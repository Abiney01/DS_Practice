# Propeers (it is based on data)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rearrange_attendees(head):
    if not head or not head.next:
        return head

    odd_head = odd_tail = None  # Head and tail for odd numbers
    even_head = even_tail = None  # Head and tail for even numbers

    current = head
    while current:
        next_node = current.next  # Save the next node
        current.next = None  # Disconnect current node

        if current.val % 2 == 1:  # Odd number
            if odd_head is None:
                odd_head = odd_tail = current
            else:
                odd_tail.next = current
                odd_tail = current
        else:  # Even number
            if even_head is None:
                even_head = even_tail = current
            else:
                even_tail.next = current
                even_tail = current
        
        current = next_node  # Move to the next node

    if odd_tail:
        odd_tail.next = even_head  # Merge odd list with even list

    return odd_head if odd_head else even_head  # Return new head of the list

# Function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print("-1")

# Function to create a linked list from a list
def create_linked_list(arr):
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


arr = [1,3,2,4,7,9,5]
head = create_linked_list(arr)
new_head = rearrange_attendees(head)
print_list(new_head)



# leetcode (it is based on positions)
def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd_pointer = head 
        even_pointer = head.next
        even_head = even_pointer
        while even_pointer is not None and even_pointer.next is not None:
            odd_pointer.next = odd_pointer.next.next
            odd_pointer = odd_pointer.next
            even_pointer.next = even_pointer.next.next
            even_pointer = even_pointer.next
        odd_pointer.next = even_head
        return head
