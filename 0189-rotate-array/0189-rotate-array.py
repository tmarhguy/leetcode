class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        size = len(nums)
        k = k%size

        nums.reverse()

        nums[:k] = reversed(nums[:k])

        nums[k:] = reversed(nums[k:])