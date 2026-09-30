class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = str(format(n, 'b'))

        num = sum([int(i) for i in binary])

        return num
        