class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = {}

        for p, w in zip(pattern, words):
            if p in mapping and mapping[p] != w:
                return False
            mapping[p] = w

        return len(mapping) == len(set(words))