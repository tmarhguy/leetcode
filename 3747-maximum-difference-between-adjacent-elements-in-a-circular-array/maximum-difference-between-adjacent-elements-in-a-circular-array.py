class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxValue = abs(nums[-1] - nums[0])

        for i in range(len(nums)-1):
            if abs(nums[i] - nums[i+1]) > maxValue:
                maxValue = abs(nums[i] - nums[i+1])
        return maxValue

        