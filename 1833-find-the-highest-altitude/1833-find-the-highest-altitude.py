class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        temp_max = float('-inf')
        temp = 0

        for num in gain:
            temp += num
            if temp > temp_max:
                temp_max = temp

        return temp_max if temp_max > 0 else 0
        