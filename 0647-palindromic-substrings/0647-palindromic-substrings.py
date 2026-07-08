class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        total = 0
        
        for i in range(n):
            total += self.countPalindromes(s, i, i)      # Odd length
            total += self.countPalindromes(s, i, i + 1)  # Even length
        
        return total
    
    def countPalindromes(self, s, left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count