class Solution(object):
    def differenceOfSum(self, nums):
        a = [int(digit) for digit in str((''.join(map(str, nums))))]
        return (sum(nums) - sum([int(digit) for digit in str((''.join(map(str, nums))))]))