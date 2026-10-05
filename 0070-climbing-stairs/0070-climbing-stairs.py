class Solution:
    def climbStairs(self, n: int) -> int:
        left, right = 1,1

        for i in range(n-1):
            temp = left
            left = right + left
            right = temp
        return left
        