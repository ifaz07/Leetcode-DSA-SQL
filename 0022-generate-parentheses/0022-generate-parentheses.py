class Solution(object):
    def generateParenthesis(self, n):
        self.result = []
        self.backtrack("", 0, 0, n)
        return self.result

    def backtrack(self, s, open, close, n):
        if len(s) == 2 * n:
            self.result.append(s)
            return

        if open < n:
            self.backtrack(s + "(", open + 1, close, n)

        if close < open:
            self.backtrack(s + ")", open, close + 1, n)