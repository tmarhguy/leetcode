class Solution(object):
    def isThree(self, n):
        factors = [] 
        for i in range(1,n+1):
            if n%i == 0:
                factors.append(i)
                
        if len(factors) == 3:
            return True
        else:
            return False