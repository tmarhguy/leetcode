class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_nums = defaultdict(int)
        result = []

        for num in nums:
            hash_nums[num] += 1
        
        count = 0

        while count < k:
            temp_max = max(hash_nums, key = hash_nums.get)
            result.append(temp_max)

            hash_nums[temp_max] = float('-inf')
            count += 1
        return result