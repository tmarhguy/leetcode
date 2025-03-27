class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            first, second = 0,1
            for i in range(n):
                third = first+ second
                first, second = second, third
            return first
        