from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins : return None 
        
        dp = [amount+1] * (amount + 1) 
        dp[0] = 0 
        
        for i in range(1,amount+1) : 
            for coin in coins : 
                if i - coin >= 0 : 
                    dp[i] = min(dp[i], dp[i-coin] +1)
        if dp[amount] != amount+1 : return dp[amount] 
        else: return -1