from queue import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def zigZag(root):
        if not root:
            return []
        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            level_nodes = deque()

            for _ in range(level_size):
                node = queue.popleft()
                if left_to_right:
                    level_nodes.append(node.val)
                else:
                    level_nodes.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.extend(level_nodes)
            left_to_right = not left_to_right

        return result

    @staticmethod
    def buildTree(nodes):
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


# Reading input
nodes = [1, 2, 3, -1, -1, -1, 6, -1, -1]
root = TreeNode.buildTree(nodes)
print(TreeNode.zigZag(root))
