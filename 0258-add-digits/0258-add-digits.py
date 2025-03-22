class Solution(object):
    def addDigits(self, num):
        num = [int(digit) for digit in str(num)]
        sum1 =sum(num)
        
        while sum1 >= 10:
            num = [int(digit) for digit in str(sum1)]
            sum1 = sum(num)
        return int(sum1)