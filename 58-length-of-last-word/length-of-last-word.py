class Solution(object):
    def lengthOfLastWord(self, s):
        n=-1
        s = s.rstrip()

        while -n <= len(s) and s[n] != " ":
            n -= 1

        return -1-n