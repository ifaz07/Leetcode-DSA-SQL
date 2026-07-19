class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = ""
        n, m = len(word1), len(word2)

        for i in range(min(n, m)):
            ans += word1[i]
            ans += word2[i]

        ans += word1[min(n, m):]
        ans += word2[min(n, m):]

        return ans