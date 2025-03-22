class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            if len(str(num)) > 1:
                temp = list(str(num))
                temp = [int(num) for num in temp]
                result += temp

            else:
                result.append(num)

        return result
        