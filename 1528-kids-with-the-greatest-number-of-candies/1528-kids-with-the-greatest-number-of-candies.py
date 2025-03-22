class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_candy = max(candies)
        
        for candy in candies:
            result.append(candy + extraCandies >= max_candy)

        return result
        