class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        cache = {}
        ans = -1
        for i in range(len(s)):
            if s[i] in cache:
                ans = max(ans, i - cache[s[i]] - 1)
            else:
                cache[s[i]] = i
        
        return ans