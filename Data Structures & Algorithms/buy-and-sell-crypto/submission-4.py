class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxP = 0

        for sell in prices:
            profit = sell - buy
            maxP = max(maxP, profit)
            buy = min(sell, buy)

        return maxP





            

        