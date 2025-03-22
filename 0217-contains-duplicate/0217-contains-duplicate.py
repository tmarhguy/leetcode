class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set()

        for number in nums:
            if number not in unique_nums:
                unique_nums.add(number)
            else:
                return True
        return False
        