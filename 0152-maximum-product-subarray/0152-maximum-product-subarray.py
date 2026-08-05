class Solution(object):
    def maxProduct(self, nums):

        ans = float('-inf')
        pre = 1
        suff = 1
        for i in range(len(nums)):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1

            pre *= nums[i]
            suff *= nums[len(nums) - i - 1]

            ans = max(ans, pre, suff)

        return ans
        