class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if max(nums) == min(nums): return 0
        numlist = defaultdict(int)
        for num in nums: numlist[num] += 1

        maxVal = 0

        for key, value in numlist.items():
            if (key+1) in numlist:
                maxVal = max(maxVal, (value + numlist[key+1]))
        return maxVal


