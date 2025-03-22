class Solution(object):
    def alternateDigitSum(self, n):
        n = [int(digit) for digit in str(n)]
        sum1 = 0
        for i in range(len(n)):
            if i%2 == 0:
                sum1 += n[i]
            else:
                sum1 -= n[i]
        return int(sum1)