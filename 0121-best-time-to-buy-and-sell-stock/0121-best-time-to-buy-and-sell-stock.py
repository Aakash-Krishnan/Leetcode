class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans= 0
        Max = prices[-1]
        for i in range(len(prices) -2 ,-1, -1):
            if prices[i] > Max:
                Max = prices[i]
            
            Sum = Max - prices[i]
            ans = max(ans, Sum)
        return ans