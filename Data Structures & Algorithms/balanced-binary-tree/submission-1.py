# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = True

        def tree_height(node):
            nonlocal balanced
            if node is None:
                return 0
            hl = tree_height(node.left)
            hr = tree_height(node.right)
            if abs(hl - hr) > 1:
                balanced = False
            return max(hl, hr) + 1

        tree_height(root)

        return balanced
