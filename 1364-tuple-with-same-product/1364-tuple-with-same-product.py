class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        seen = defaultdict(set)
        count = 0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prod = nums[i] * nums[j]
                if (nums[i],nums[j]) not in seen[prod]:
                    seen[prod].add((nums[i],nums[j]))
        for _, value in seen.items():
            if len(value) == 2:
                count += 1
            elif len(value) > 2:
                count += math.comb(len(value), 2)
        return count * 8
        