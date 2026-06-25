from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        deq = deque([root])

        while deq:
            level = []
            level_size = len(deq)
            
            for _ in range(level_size):
                node = deq.popleft()
                level.append(node.val)
                
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            
            result.append(level)
            
        return result