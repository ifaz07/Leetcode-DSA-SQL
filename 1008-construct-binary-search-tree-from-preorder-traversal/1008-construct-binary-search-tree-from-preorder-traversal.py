class Solution(object):
    def bstFromPreorder(self, preorder):

        self.idx = 0
        self.preorder = preorder
        return self.build(float('inf'))
    
    def build(self, upper_bound):
        if self.idx == len(self.preorder) or self.preorder[self.idx] > upper_bound:
            return None
        
        root = TreeNode(self.preorder[self.idx])
        self.idx += 1
        
        root.left = self.build(root.val)
        root.right = self.build(upper_bound)
        
        return root