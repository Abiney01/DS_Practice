from typing import List, Optional
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

from typing import List

def buildBinaryTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildBinaryTree(preorder[1:mid+1],inorder[:mid])
    root.right = buildBinaryTree(preorder[mid+1:],inorder[mid+1:])
    return root
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print(buildBinaryTree(preorder,inorder))