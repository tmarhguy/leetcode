class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        mid = total // 2

        p = [False] * (mid + 1)
        p[0] = True

        for num in nums:
            for i in range(mid, num-1, -1):
                p[i] = p[i] or p[i - num]
        return p[mid]