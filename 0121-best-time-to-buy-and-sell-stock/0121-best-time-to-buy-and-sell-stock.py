class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left, right = 0, 1

        maxP = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                maxP = max(maxP, prices[right] - prices[left])

            right += 1
        return maxP
        