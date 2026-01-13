class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            # reverse the group
            prev = groupNext
            curr = groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # reconnect
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" → ".join(result))

head = build_linked_list([1, 2, 3, 4, 5])
k = 2
sol = Solution()
result = sol.reverseKGroup(head, k)
print_linked_list(result)
