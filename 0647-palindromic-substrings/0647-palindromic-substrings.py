class Solution:
    def countSubstrings(self, s: str) -> int:
        def palamdrome(L, R):
            nonlocal res
            if L < 0 or R == len(s):
                return 
            if s[L] == s[R]:
                res += 1
                palamdrome(L-1, R + 1)
            return 
        
        res = 0
        for i in range(len(s)):
            res += 1
            odd = palamdrome(i-1, i+1)
            even = palamdrome(i, i+1)
        
        return res