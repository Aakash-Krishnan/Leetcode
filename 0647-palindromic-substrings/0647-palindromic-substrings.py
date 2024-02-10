class Solution:
    def countSubstrings(self, s: str) -> int:
        def palamdrome(L, R):
            cnt = 0
            while L > -1 and R < len(s) and s[L] == s[R]:
                cnt += 1
                L -= 1
                R += 1
            return cnt
        
        res = 0
        for i in range(len(s)):
            res += palamdrome(i, i)
            res += palamdrome(i, i+1)
        return res