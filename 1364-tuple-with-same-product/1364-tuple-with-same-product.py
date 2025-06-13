class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        count = 0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prod = nums[i] * nums[j]
                seen[prod] += 1
        for value in seen.values():
            if value >= 2:
                count += int(value * (value - 1) / 2)
        return count * 8
        