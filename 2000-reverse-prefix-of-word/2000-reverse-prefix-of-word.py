class Solution(object):
    def reversePrefix(self, word, ch):
        rev = ""
        for i in range(len(word)):
            rev = word[i] + rev
            if word[i] == ch:
                return rev + word[i+1:]
        return word