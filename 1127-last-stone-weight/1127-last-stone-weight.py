class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        i = len(stones) - 1

        while len(stones) > 1:
            diff = stones[i] - stones[i-1]
            if diff > 0:
                stones = stones[:-1]
                stones[-1] = diff
                stones.sort()
                i -= 1
            elif diff == 0:
                stones = stones[:-2]
                i -= 2
        return stones[0] if stones else 0

        