
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        self._height(root)
        return self.diameter
    
    def _height(self, node):
        if not node:
            return 0
        
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        
        self.diameter = max(self.diameter, left_height + right_height)
        
        return 1 + max(left_height, right_height)