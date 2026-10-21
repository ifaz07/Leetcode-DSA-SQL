class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = ""

        num = num & 0xFFFFFFFF

        while num:
            remainder = num % 16
            result = hex_chars[remainder] + result
            num = num // 16

        return result