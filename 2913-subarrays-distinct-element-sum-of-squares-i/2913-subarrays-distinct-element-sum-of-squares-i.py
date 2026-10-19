class Solution(object):
    def sumCounts(self, nums):
        total = 0
        n = len(nums)

        for i in range(n):
            s = set()
            for j in range(i, n):
                s.add(nums[j])
                total += len(s) * len(s)

        return total