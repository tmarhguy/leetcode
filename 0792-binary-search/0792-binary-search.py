class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        stop = len(nums) - 1

        while start <= stop:
            mid = int((start+stop)/2)
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                stop = mid - 1
            elif target == nums[mid]:
                return mid
        return -1
        