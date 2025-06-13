class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hash set
        hash_nums = {}

        for i,num in enumerate(nums):
            complement = target - num
            if complement not in hash_nums:
                hash_nums[num] = i
            else:
                return [hash_nums[complement], i]

        