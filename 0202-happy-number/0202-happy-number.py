class Solution(object):
    def isHappy(self, n):
        
        if n == 7 or n == 10: return True
        else:
            while n > 10:
                lst = []
                n = str(n)
                n = list(n)
                n = [int(i) for i in n]
                m = 0
                for a in n:
                    m += a**2
                    n = m

            if n == 1 or n == 7 or n == 10: return True
            else: return False