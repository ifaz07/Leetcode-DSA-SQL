class Solution(object):
    def helper(self, candidates, target, start, path):
        if target == 0:
            self.ans.append(path[:])
            return

        if target < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            self.helper(candidates, target - candidates[i], i, path)
            path.pop()

    def combinationSum(self, candidates, target):
        self.ans = []
        self.helper(candidates, target, 0, [])
        return self.ans