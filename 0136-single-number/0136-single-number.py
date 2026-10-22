class Solution(object):
    def singleNumber(self, nums):
        single = 0
        for i in nums:
            single ^= i
        
        return single