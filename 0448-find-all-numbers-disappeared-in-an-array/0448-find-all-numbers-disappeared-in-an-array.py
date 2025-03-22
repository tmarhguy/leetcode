class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setA = set(nums)
        n = len(nums) + 1
        
        listB = [i for i in range(1,n)]
        
        setB = set(listB)
        
        answer = setB - setA
        
        return list(answer)
        