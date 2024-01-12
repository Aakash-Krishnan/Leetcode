
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        cache = set('aeiouAEIOU')
        mid = len(s) // 2
        cnt1, cnt2 = 0, 0
        for i in range(len(s)):
            if s[i] in cache:
                if 0 <= i < mid:
                    cnt1 += 1
                else:
                    cnt2 += 1
        
        return cnt1 == cnt2
        
        