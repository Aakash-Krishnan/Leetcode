class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        
        return dp[amount] if dp[amount] != (amount + 1) else -1
    
    
#         cache = [[-1] * (amount + 1) for _ in range(len(coins))] 
        
#         def dfs(i, remainder):
#             if remainder == 0:
#                 return 0
#             if i >= len(coins) or remainder < 0:
#                 return float("inf")
            
#             if cache[i][remainder] != -1:
#                 return cache[i][remainder]
            
            
#             res = min(dfs(i+1, remainder), 1 + dfs(i, remainder - coins[i]))
            
#             cache[i][remainder] = res
#             return res
        
#         ans = dfs(0, amount)
#         return ans if ans != float('inf') else -1
    