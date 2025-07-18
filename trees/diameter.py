class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diameterOfBinaryTree(root: TreeNode) -> int:
    res = [0]
    def dfs(root):
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)
        res[0] = max(res[0],2+left+right)
        return 1 + max(left,right)
    dfs(root)
    return res[0]