class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_nums = {}

        for index, number in enumerate(nums):
            complement = target - number
            if complement not in hash_nums:
                hash_nums[number] = index
            else:
                return [hash_nums[complement], index]
        