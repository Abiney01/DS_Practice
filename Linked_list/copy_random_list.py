class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # 1️⃣ Insert copied nodes after originals
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next

        # 2️⃣ Assign random pointers
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 3️⃣ Separate the two lists
        dummy = Node(0)
        copy_cur = dummy
        cur = head

        while cur:
            copy_cur.next = cur.next
            cur.next = cur.next.next
            cur = cur.next
            copy_cur = copy_cur.next

        return dummy.next

# Create nodes
a = Node(1)
b = Node(2)
c = Node(3)

# Next pointers
a.next = b
b.next = c

# Random pointers
a.random = c
b.random = a
c.random = b

# Copy list
sol = Solution()
copied_head = sol.copyRandomList(a)

# Print copied list
cur = copied_head
while cur:
    print(
        "Val:", cur.val,
        "Random:", cur.random.val if cur.random else None
    )
    cur = cur.next
