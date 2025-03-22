class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        total = 0
        for char in str(n):
            total += int(char)
            prod *= int(char)
        return prod - total

        