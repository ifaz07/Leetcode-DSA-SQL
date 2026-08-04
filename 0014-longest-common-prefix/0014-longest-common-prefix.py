class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for str in strs[1:]:
                if i >= len(str) or str[i] != char:
                    return strs[0][:i]
        return strs[0]