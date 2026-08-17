class Solution(object):
    def largestRectangleArea(self,arr):
        stack = []
        ans = 0
        n = len(arr)

        for i in range(n + 1):
            curr = 0 if i == n else arr[i]

            while stack and arr[stack[-1]] > curr:
                height = arr[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                ans = max(ans, height * width)

            stack.append(i)

        return ans