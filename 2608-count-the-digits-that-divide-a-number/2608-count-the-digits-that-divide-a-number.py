class Solution(object):
    def countDigits(self, num):
        lst = [int(digit) for digit in str(num)]
        count = 0
        for digit in lst:
            if num%digit == 0:
                count += 1

        return count