class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        stop = len(s)-1

        while start < stop:
            if start <= len(s)-1 and stop >= 0:
                if s[start] == s[stop]:
                    start += 1
                    stop -= 1
                elif not s[start].isalnum():
                    start += 1
                elif not s[stop].isalnum():
                    stop -= 1
                else:
                    return False
        return True
        