class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, res = 0, 0
        for r in range(len(prices)):
            if r > 0 and prices[r] < prices[r-1]:
                res += prices[r-1] - prices[l]
                l = r
        res += prices[-1] - prices[l]
        return res        