class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_nums:
                return [hash_nums[complement], i]
            else:
                hash_nums[num] = i
        