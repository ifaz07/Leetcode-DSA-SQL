class Solution(object):

    def dfs(self, node, current):
        if not node:
            return 0

        current = current * 10 + node.val

        if not node.left and not node.right:
            return current

        return self.dfs(node.left, current) + self.dfs(node.right, current)

    def sumNumbers(self, root):
        return self.dfs(root, 0)