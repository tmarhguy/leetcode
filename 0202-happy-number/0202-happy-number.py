class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(n):
            total = 0
            while n > 0:
                total += (n % 10) ** 2
                n //= 10
            return total
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = happy(n)

        return n == 1
        