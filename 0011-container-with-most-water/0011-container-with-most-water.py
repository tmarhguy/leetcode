class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, temp_max = 0,(len(height) - 1),0

        while left < right:
            area = min(height[left], height[right]) * (right - left)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            if area > temp_max:
                temp_max = area 
            
        return temp_max
        