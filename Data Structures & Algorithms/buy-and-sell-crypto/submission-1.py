class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        prof = 0

        for i in range(len(prices)):
            curBuy = prices[i]
            for j in range(i + 1, len(prices)):
                curSell = prices[j]
                prof = max(prof, curSell - curBuy)

        return prof


        