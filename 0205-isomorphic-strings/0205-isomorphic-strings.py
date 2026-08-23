class Solution(object):
    def isIsomorphic(self, s, t):

        if len(s) != len(t):
            return False
        
        map_s = [-1] * 128
        map_t = [-1] * 128
        
        for i in range(len(s)):
            c1 = ord(s[i])
            c2 = ord(t[i])
            
            if map_s[c1] == -1 and map_t[c2] == -1:
                map_s[c1] = c2
                map_t[c2] = c1
            elif map_s[c1] != c2 or map_t[c2] != c1:
                return False
        
        return True