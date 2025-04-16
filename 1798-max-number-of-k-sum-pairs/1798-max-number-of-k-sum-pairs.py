class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hash_nums = defaultdict(int)
        count = 0

        for num in nums:
            complement = k - num
            if hash_nums[complement] > 0:
                count += 1
                hash_nums[complement] -= 1
            else:
                hash_nums[num] += 1

        return count
