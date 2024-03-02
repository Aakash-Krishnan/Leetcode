class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        @cache
        def dfs(i):
            if i >= len(prices):
                return 0
            res = float("inf")
            for j in range(i+2):
                res = min(res, dfs(i+j+1) + prices[i])
            return res
 
        return dfs(0)