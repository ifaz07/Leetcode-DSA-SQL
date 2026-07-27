
class Solution(object):
    def countNodes(self, root):
        if root == None:
            return 0

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)