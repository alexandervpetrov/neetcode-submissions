# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()

        if root is not None:
            queue.append(root)

        rights = []
        while queue:
            level_size = len(queue)
            last_item = None
            for __ in range(level_size):
                node = queue.popleft()
                last_item = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            rights.append(last_item)
        
        return rights
