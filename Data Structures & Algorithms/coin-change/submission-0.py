class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1) # goes from 0 to amount index
        # base case
        dp[0] = 0
        
        for a in range(1, amount+1):
            for coin in coins:
                if a - coin >= 0:
                    # dp at a is min of curr dp or 1 + dp of amount - coin
                    dp[a] = min(dp[a], 1 + dp[a-coin])

        return dp[amount] if dp[amount] != amount+1 else -1


