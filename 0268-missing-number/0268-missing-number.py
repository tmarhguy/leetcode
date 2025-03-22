class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        setA = set(nums)
        setB = set()

        for i in range(len(nums)+ 1):
            setB.add(i)

        result = list(setB-setA)
        
        return result[0]
        """
        
        result = 0

        for i in range(len(nums) + 1):
            result ^= i
        
        for num in nums:
            result ^= num
        
        return int(result)