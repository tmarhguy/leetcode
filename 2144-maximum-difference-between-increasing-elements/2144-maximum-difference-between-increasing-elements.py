class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minVal = nums[0]
        maxDiff = -1

        for i in range(1,len(nums)):
            if nums[i] > minVal:
                maxDiff = max(maxDiff, nums[i] - minVal)
            else:
                minVal = nums[i]
        return maxDiff