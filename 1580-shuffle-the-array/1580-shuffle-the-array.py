class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        i = 0
        while i < len(nums)/2:
            result.append(nums[i])
            result.append(nums[n+i])
            i += 1
        return result
        