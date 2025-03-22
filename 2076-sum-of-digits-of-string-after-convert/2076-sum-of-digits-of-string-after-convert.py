class Solution(object):
    def getLucky(self, s, k):
        num = []
        for i in s:
            num.append(str(ord(i) - 96))
            a = (''.join(num))
            a = [int(digit) for digit in str(a)]

        sum1 = 0

        for i in range(k):
            sum1 = sum(a)
            a = [int(digit) for digit in str(sum1)]
        return (int(sum1))