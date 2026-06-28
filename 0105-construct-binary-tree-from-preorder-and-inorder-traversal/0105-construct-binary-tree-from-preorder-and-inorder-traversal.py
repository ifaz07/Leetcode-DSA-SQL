# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        self.preorder_index = 0
        self.inorder_map = {}

        for index, value in enumerate(inorder):
            self.inorder_map[value] = index
        
        return self._build_tree(preorder, 0, len(inorder) - 1)
    
    def _build_tree(self, preorder, left, right):
        if left > right:
            return None

        root_val = preorder[self.preorder_index]
        self.preorder_index += 1

        root = TreeNode(root_val)
        root_index = self.inorder_map[root_val]

        root.left = self._build_tree(preorder, left, root_index - 1)
        root.right = self._build_tree(preorder, root_index + 1, right)
        
        return root