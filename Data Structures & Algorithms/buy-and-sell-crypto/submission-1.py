class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minP = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minP)
            minP = min(minP, sell)

        return maxP