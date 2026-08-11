class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()

        j = len(s) - 1

        for i in range(len(s)):
            
            if i >= j:
                break

            if not (('a' <= s[i] <= 'z') or ('0' <= s[i] <= '9')):
                continue

            while j > i and not (
                ('a' <= s[j] <= 'z') or
                ('0' <= s[j] <= '9')
            ):
                j -= 1

            if s[i] != s[j]:
                return False

            j -= 1

        return True