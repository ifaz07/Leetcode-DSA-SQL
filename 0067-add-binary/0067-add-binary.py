class Solution(object):
    def addBinary(self, a, b):
        totalSum = ""
        carry = 0

        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0

            total = x + y + carry

            totalSum += str(total % 2)
            carry = total // 2

            i -= 1
            j -= 1

        return totalSum[::-1]