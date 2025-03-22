class Solution(object):
    def separateDigits(self, nums):
        nums = ''.join(map(str,nums))
        return [int(digit) for digit in nums]