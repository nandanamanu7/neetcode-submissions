class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - buy
            if(profit > maxProfit):
                maxProfit = profit 
            buy = min(prices[i], buy)

        return maxProfit





            

        