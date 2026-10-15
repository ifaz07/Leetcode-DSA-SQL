class Solution(object):
    def findTheDifference(self, s, t):
        
        total1 = 0
        total2 = 0
        for i in range(len(s)):
            total1 += ord(s[i])
            total2 += ord(t[i])

        total2 += ord(t[len(t)-1])
        return chr(total2-total1)

