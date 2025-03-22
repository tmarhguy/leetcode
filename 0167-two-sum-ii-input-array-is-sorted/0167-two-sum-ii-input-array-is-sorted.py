class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, stop = 0,len(numbers)-1

        if len(numbers) < 2:
            return []

        while start<stop:
            current = numbers[start] + numbers[stop]

            if current == target:
                return [start+1,stop+1]
            elif current > target:
                stop -= 1
            elif current < target:
                start += 1
            
        return []
