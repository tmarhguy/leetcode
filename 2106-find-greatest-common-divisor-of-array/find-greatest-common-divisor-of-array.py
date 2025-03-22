class Solution(object):
    def findGCD(self, nums):
        a = min(nums)
        b = max(nums)
        
        while not a == b:
            if a > b:
                a -= b
            else:
                b -= a
        return int(a)
        
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        