from collections import deque
class TreeNode:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

def build_tree(nodes):
    if not nodes or nodes[0] == -1:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while i < len(nodes):
        current = queue.popleft()

        if i < len(nodes) and nodes[i] != -1:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1

        if i < len(nodes) and nodes[i] != -1:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1

    return root
def leftView(root):
    if not root:
        return []
    result = []
    queue = deque([(root,0)])
    seen_levels = set()
    while queue:
        node,levels = queue.popleft()
        if levels not in seen_levels:
            result.append(node.data)
            seen_levels.add(levels)
        if node.left:
            queue.append((node.left,levels+1))
        if node.right:
            queue.append((node.right,levels+1))   #--> same right view only difference is node.right come first
    return result

nodes = [3,4,-1,-1,-1]
root = build_tree(nodes)
print(*leftView(root))