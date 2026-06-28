# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self._is_mirror(root.left, root.right)
    
    def _is_mirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        
        return self._is_mirror(left.left, right.right) and self._is_mirror(left.right, right.left)