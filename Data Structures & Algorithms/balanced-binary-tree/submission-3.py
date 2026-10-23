# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True

        balanced = {}
        heights = {}

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
                stack.append((node, AFTER_RIGHT))
                if node.right is not None:
                    stack.append((node.right, START))
            else:
                hl = heights.get(node.left, 0)
                hr = heights.get(node.right, 0)
                heights[node] = max(hl, hr) + 1
                bl = balanced.get(node.left, True)
                br = balanced.get(node.right, True)
                current_balanced = abs(hl - hr) <= 1
                balanced[node] = bl and br and current_balanced

        return balanced.get(root, True)

