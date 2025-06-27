from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrderTraversal(root):
    if not root:
        return []

    # Dictionary to store nodes by column index
    column_table = defaultdict(list)
    
    # Queue for BFS: stores (node, x-position, y-position)
    queue = deque([(root, 0, 0)])

    while queue:
        node, x, y = queue.popleft()
        
        if node:
            column_table[x].append((y, node.val))  # Store nodes by X position

            # Left child (X-1, Y-1)
            queue.append((node.left, x - 1, y - 1))
            # Right child (X+1, Y-1)
            queue.append((node.right, x + 1, y - 1))

    # Sort dictionary keys (X values)
    sorted_columns = sorted(column_table.keys())

    result = []
    for col in sorted_columns:
        # Sort by Y (descending), then by value
        column_table[col].sort(key=lambda pair: (-pair[0], pair[1]))
        result.extend(val for _, val in column_table[col])

    return result

# Helper function to build tree from level order input
def buildTree(values):
    if not values or values[0] == -1:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if values[i] != -1:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] != -1:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


nodes = [3, 9, 20, -1, -1, 15, 7]
tree = buildTree(nodes)
print(*verticalOrderTraversal(tree))
