class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)

        # base case
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if (c <= a): 
                    dp[a] = min(1 + dp[a-c], dp[a])

        if dp[amount] == float('inf'):
            return -1 
        
        return dp[amount]
                   


