class Solution:
    def minOperations(self, s: str) -> int:
        ans = 0
        
        for i in range(len(s)):
            if i % 2:
                ans += 1 if s[i] == "1" else 0
            else:
                ans += 1 if s[i] == "0" else 0
                
        return min(ans, len(s) - ans)