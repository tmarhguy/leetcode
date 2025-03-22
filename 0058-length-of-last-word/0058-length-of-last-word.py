class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #s = s.strip()
        count = 0
        size = len(s)

        for i in range(size - 1,-1,-1):
            if count >= 0 and not s[i] == " ":
                count += 1
            elif count > 0 and s[i] == " ":
                return count
        return count