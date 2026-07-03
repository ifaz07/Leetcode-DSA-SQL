# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findTarget(self, root, k):

        seen = set()
        return self._dfs(root, k, seen)
    
    def _dfs(self, node, k, seen):

        if not node:
            return False

        complement = k - node.val
        if complement in seen:
            return True
        
        seen.add(node.val)
  
        return self._dfs(node.left, k, seen) or self._dfs(node.right, k, seen)