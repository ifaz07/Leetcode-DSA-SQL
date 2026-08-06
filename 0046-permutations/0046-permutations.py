class Solution(object):
    def permute(self, nums):
        self.ans = []
        self.backtrack(0,nums)
        return self.ans

    def backtrack(self,idx,nums):

        if idx == len(nums):
            self.ans.append(nums[:]) # her this is mainly used when we want the copy 
            return 
        
        for i in range(idx,len(nums)):
            nums[idx],nums[i] = nums[i], nums[idx]
            self.backtrack(idx+1,nums)
            nums[idx],nums[i] = nums[i], nums[idx] # so that true array is not distorted 
        

