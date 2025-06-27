class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def detectAndRemoveLoop(head):
    if not head or not head.next:
        return head  # No loop possible with 0 or 1 node

    slow, fast = head, head

    # Step 1: Detect loop using Floyd’s Cycle-Finding Algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Loop detected
            print("True")
            break
    else:
        print("False")
        return head  # No loop found

    # Step 2: Find the start of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Step 3: Remove the loop
    while fast.next != slow:
        fast = fast.next
    fast.next = None  # Break the loop

    return head  # Return updated linked list

# Helper function to print the linked list
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Helper function to create a loop in the linked list
def createLoop(head, pos):
    if pos == -1:
        return head
    loop_start, temp = None, head
    index = 0

    while temp.next:
        if index == pos:
            loop_start = temp
        temp = temp.next
        index += 1
    temp.next = loop_start  # Creating the loop

    return head

# Sample Test Case
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

# Creating a loop from the last node to the second node (index 1)
head = createLoop(head,1)

# Detect and remove the loop
head = detectAndRemoveLoop(head)

# Print the updated linked list
printList(head)
