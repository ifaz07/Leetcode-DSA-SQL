
class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False

        add = 1
        i = 2

        while i * i <= num:
            if num % i == 0:
                add += i

                if i != num // i:
                    add += num // i

            i += 1

        return add == num
