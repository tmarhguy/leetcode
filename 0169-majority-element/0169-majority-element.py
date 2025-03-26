class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        temp = nums[0]

        for i in range(1,len(nums)):
            if nums[i] == temp:
                count += 1
            else:
                if count > 0:
                    count -= 1
                elif count == 0:
                    temp = nums[i]
                
        return temp
            