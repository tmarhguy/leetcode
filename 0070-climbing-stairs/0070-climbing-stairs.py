class Solution:
    def __init__(self):
        self.memo = {}
        
    def climbStairs(self, n):
        if n in self.memo:
            return self.memo[n]
        
        if n == 1:
            self.memo[n] = 1
        elif n == 2:
            self.memo[n] = 2
        else:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return self.memo[n]