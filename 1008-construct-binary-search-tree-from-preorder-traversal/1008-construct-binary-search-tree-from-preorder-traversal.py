# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
