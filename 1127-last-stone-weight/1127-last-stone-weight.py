class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            diff = stones[-1] - stones[-2]
            if diff > 0:
                stones = stones[:-1]
                stones[-1] = diff
                stones.sort()
            elif diff == 0:
                stones = stones[:-2]
        return stones[0] if stones else 0
        