class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp
        
#         res = [0]
        
#         for i in range(1, n+1):
#             pos = 0
#             cnt = 0
#             while i >> pos:
#                 cnt += (i>>pos) & 1
#                 pos += 1
            
#             res.append(cnt)
        
#         return res