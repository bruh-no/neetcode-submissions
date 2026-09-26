class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #Initialize Condition for Sliding Window to Move
        maxProf = 0

        #Initialize Pointers
        l, r = 0, 1


        #Iterate through prices and calculate maxprofit for each iteration, moving left pointer only if maxProfit was worse
        while r < len(prices):
            if prices[r] > prices[l]:
                maxProf = max(maxProf,prices[r] - prices[l])
            else:
                l = r
            r += 1
        
        return maxProf




        