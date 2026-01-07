class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # 1️⃣ Find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2️⃣ Reverse second half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 3️⃣ Merge two halves
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" → ".join(res))

head = build_list([2, 4, 6, 8])
Solution().reorderList(head)
print_list(head)