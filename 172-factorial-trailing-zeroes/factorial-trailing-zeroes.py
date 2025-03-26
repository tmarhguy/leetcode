class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        #count powers of 5
        count = 0

        while n >= 5:
            n =  n//5
            count += n
        return count