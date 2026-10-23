# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        index = {v: i for i, v in enumerate(inorder)}

        def make_tree(pi, l, r):
            if l >= r:
                return None
            v = preorder[pi]
            root = TreeNode(v)
            root_pos = index[v]
            n_left = root_pos - l
            root.left = make_tree(pi + 1, l, root_pos)
            root.right = make_tree(pi + 1 + n_left, root_pos + 1, r)
            return root

        return make_tree(0, 0, len(inorder))