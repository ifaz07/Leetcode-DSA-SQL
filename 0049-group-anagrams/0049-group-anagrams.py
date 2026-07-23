class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - 97] += 1

            key = ""
            for x in count:
                key += "#" + str(x)

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        ans = []
        for key in groups:
            ans.append(groups[key])

        return ans