from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        
        maxW = 0
        deq = deque([(root,0)])

        while deq:

            level_min = deq[0][1]
            maxW = max(maxW, deq[-1][1] - deq[0][1]+1)
            for _ in range(len(deq)):
                node,idx = deq.popleft()
                normalized = idx - level_min
                if node.left:
                    deq.append((node.left,normalized*2+1))
                if node.right:
                    deq.append((node.right,normalized*2+2))
        
        return maxW
