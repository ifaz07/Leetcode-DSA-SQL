class Solution(object):
    def getNext(self, n):
        total = 0
        while n:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total

    def isHappy(self, n):
        slow = n
        fast = n

        while True:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))

            if fast == 1:
                return True

            if slow == fast:
                return False