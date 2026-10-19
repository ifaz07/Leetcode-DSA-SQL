class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        idx= []

        for i in range(len(nums)):
            if nums[i] == target:
                idx.append(i)
            
        return idx