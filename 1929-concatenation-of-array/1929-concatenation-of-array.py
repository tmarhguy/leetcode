class Solution(object):
    def getConcatenation(self, nums):
        size = len(nums)
        ans = [0 for x in range(2 * size)]

        for i in range(size):
            ans[i] = nums[i]
            ans[i+size] = nums[i]
        return ans