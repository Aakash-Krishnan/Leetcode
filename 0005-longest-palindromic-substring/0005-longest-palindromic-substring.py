class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def palandrome(s, L, R):
            while L > -1 and R < len(s):
                if s[L] != s[R]:
                    break
                L -= 1
                R += 1
            return s[L+1:R]
        
        ans = ''
        
        for i in range(len(s)):
            Max = ''
            odd = palandrome(s, i-1, i+1)
            even = palandrome(s, i, i+1)
            
            if len(odd) > len(even):
                if len(ans) < len(odd):
                    ans = odd
            else:
                if len(ans) < len(even):
                    ans = even
                
        return ans