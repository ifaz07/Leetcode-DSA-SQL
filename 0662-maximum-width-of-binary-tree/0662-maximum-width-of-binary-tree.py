from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        ans = 0
        q = deque([(root, 0)])
        while q:
            size = len(q)
            level_min = q[0][1]
            ans = max(ans, q[-1][1] - q[0][1] + 1)
            
            for _ in range(size):
                node, idx = q.popleft()
                normalized = idx - level_min
                if node.left:
                    q.append((node.left, normalized * 2 + 1))
                if node.right:
                    q.append((node.right, normalized * 2 + 2))
        return ans