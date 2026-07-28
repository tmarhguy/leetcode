class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        state = 0
        ptr = 0

        for num in nums:
            if num == 1:
                ptr += 1
                state = max(state, ptr)
            else:
                ptr = 0

        return state
