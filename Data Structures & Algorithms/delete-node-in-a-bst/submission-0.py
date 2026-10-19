# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def find_min_node(root):
    current = root
    while current is not None and current.left is not None:
        current = current.left
    return current


class Solution:
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                min_node = find_min_node(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        
        return root
        

        