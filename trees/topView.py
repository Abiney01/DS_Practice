from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def top_view(root):
    if not root:
        return []

    queue = deque([(root, 0)])  # (node, horizontal distance)
    top_nodes = {}

    min_hd, max_hd = 0, 0

    while queue:
        node, hd = queue.popleft()

        if hd not in top_nodes:
            top_nodes[hd] = node.val

        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    return [top_nodes[i] for i in range(min_hd, max_hd + 1)]

# Sample tree construction
def build_tree(arr):
    if not arr or arr[0] == -1:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        if arr[i] != -1:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr[i] != -1:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

# Sample Input 1
arr1 = [1, 2, 3, 4, 5, -1, 6, -1, 7, -1, -1, 8, -1, 9, -1, -1, 11, 10, -1, -1, -1, -1, -1]
root1 = build_tree(arr1)
print(top_view(root1))  # Output: [10, 4, 2, 1, 3, 6]

# Sample Input 2
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
root2 = build_tree(arr2)
print(top_view(root2))  # Output: [8, 4, 2, 1, 3, 7]
