class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        best = float('-inf')

        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            best = max(best, prices[r] - prices[l])
        return best
        