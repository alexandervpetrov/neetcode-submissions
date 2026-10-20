# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = 0
        kth = None

        def visit(node):
            nonlocal kth, count
            if node is None:
                return
            visit(node.left)
            count += 1
            if count == k:
                kth = node.val
            if count >= k:
                return
            visit(node.right)

        visit(root)
        return kth
