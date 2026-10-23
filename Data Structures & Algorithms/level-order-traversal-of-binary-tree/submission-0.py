# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque()

        if root is not None:
            queue.append(root)

        levels = []
        while queue:
            level_size = len(queue)
            level_items = []
            for __ in range(level_size):
                node = queue.popleft()
                level_items.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            levels.append(level_items)
        
        return levels
            





