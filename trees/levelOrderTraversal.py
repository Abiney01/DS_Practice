from queue import deque
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def getLevelOrder(root):
    if not root:
        return []
    res = []
    q = deque([root])

    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res


# leetcode
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            level_size = len(q)  
            level = []
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res