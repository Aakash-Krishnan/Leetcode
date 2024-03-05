class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 1:
            return 1
        l, r = 0, len(s)-1
        while l<=r:
            if l != r and s[l] == s[r]:
                while l + 1 < r and s[l+1] == s[r]:
                    l += 1
                while r - 1 > l and s[r-1] == s[l]:
                    r -= 1
                l += 1
                r -= 1
            else:
                return r - l + 1
        
        return 0