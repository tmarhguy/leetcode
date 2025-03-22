class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if needle == haystack[i:i+len(needle)] and (i+len(needle)) <= len(haystack):
                return i
        return -1
        