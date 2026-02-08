class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self,head,left,right):
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        # Move prev and current to correct positions
        for _ in range(left - 1):
            prev = prev.next
            current = current.next

        preNode = None
        subListHead = current

        # Reverse the sublist
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = preNode
            preNode = current
            current = next_node

        # Reconnect
        prev.next = preNode
        subListHead.next = current

        return dummy.next

def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res))
head = build_linked_list([1, 2, 3, 4, 5])
left, right = 2, 4

sol = Solution()
result = sol.reverseBetween(head, left, right)
print_linked_list(result)
