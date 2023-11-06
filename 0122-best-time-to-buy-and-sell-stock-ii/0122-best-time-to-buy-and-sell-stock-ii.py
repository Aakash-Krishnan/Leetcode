class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        cnt = 0
        Max = prices[-1]
        
        for i in range(len(prices)-2, -1, -1):
            if prices[i] > Max:
                Max = prices[i]
                cnt = 0
            else:
                val = Max - prices[i]
                if val > cnt:
                    ans -= cnt
                    cnt = val
                    ans += cnt
                else:
                    Max = prices[i]
                    cnt = 0
        
        return ans