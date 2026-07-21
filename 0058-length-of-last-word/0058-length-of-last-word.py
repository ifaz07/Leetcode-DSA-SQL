class Solution(object):
    def lengthOfLastWord(self, s):
        
        cnt = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                cnt += 1
            
            elif s[i] == " " and cnt != 0:
                return cnt

        return cnt
            
        