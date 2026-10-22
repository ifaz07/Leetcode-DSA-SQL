class Solution(object):
    def hammingDistance(self, x, y):
        num = x ^ y
        count = 0

        while num:
            count += num % 2
            num = num // 2

        return count