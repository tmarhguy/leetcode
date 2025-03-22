class Solution(object):
    def mySqrt(self, x):
        n = 0
        while(x > n * n):
            n = n + 1
        if x == n*n:
            return n
        elif x != n*n and x < n*n:
            return (int(n - 1))
        
        """
        :type x: int
        :rtype: int
        """
        