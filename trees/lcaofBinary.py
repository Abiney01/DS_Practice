class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lowestCommonAncestor(root, x: int, y: int) -> int:
    if root is None:
        return None
    
    # If root is X or Y, return root
    if root.data == x or root.data == y:
        return root.data

    # Recur for left and right subtree
    left_lca = lowestCommonAncestor(root.left, x, y)
    right_lca = lowestCommonAncestor(root.right, x, y)

    # If both left and right subtree return non-None values, root is the LCA
    if left_lca is not None and right_lca is not None:
        return root.data

    # Otherwise return the non-None result
    return left_lca if left_lca is not None else right_lca
