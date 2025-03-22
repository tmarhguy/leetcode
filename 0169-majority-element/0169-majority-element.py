class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_nums = defaultdict(int)

        for num in nums:
            hash_nums[num] += 1
        
        max_count = max(hash_nums, key = hash_nums.get)

        return max_count
        