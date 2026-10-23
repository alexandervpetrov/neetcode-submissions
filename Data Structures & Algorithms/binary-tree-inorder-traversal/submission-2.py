# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        values = []

        if root is None:
            return values

        START = 0
        AFTER_LEFT = 1
        AFTER_RIGHT = 2

        stack = [(root, START)]
        while stack:
            node, state = stack.pop()
            if state == START:
                stack.append((node, AFTER_LEFT))
                if node.left is not None:
                    stack.append((node.left, START))
            elif state == AFTER_LEFT:
                values.append(node.val)
                stack.append((node, AFTER_RIGHT))
                if node.right is not None:
                    stack.append((node.right, START))
            else:
                pass

        return values

