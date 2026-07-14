class Solution(object):
    def divide(self, dividend, divisor):

        a =int(float(dividend)/divisor)
        if a>2**31-1:
            return 2**31-1
        elif a<-2**31:
            return -2**31
        else:
            return a
