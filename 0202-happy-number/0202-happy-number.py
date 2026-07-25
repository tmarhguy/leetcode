class Solution(object):
    def isHappy(self, n):
        temp = []
        seen = set()

        while (n != 1):
            temp = [(int(x))**2 for x in str(n)]
            n = sum(temp)
            if n not in seen:
                seen.add(n)
            else:
                return False
        return True
        