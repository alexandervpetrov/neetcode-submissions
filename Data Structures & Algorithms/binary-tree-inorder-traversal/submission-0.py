# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        values = []

        def visit(root):
            if root is None:
                return
            visit(root.left)
            values.append(root.val)
            visit(root.right)

        visit(root)
        return values