from collections import deque

class Solution(object):
    def averageOfLevels(self, root):

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            total = 0

            for _ in range(level_size):
                node = queue.popleft()
                total += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(float(total) / level_size)

        return result