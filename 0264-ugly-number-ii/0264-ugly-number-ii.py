class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        x = y = z = 0
        for i in range(1, n):
            v2 = dp[x] * 2
            v3 = dp[y] * 3
            v5 = dp[z] * 5
            dp[i] = min(v2, v3, v5)
            if dp[i] == v2:
                x += 1
            if dp[i] == v3:
                y += 1
            if dp[i] == v5:
                z += 1
        
        return dp[n-1]