class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        ans = 0
        
        for i in range(len(s)):
            fmap = {}
            cnt = 0
            for j in range(i, len(s)):
                if s[j] not in fmap:
                    fmap[s[j]] = 1
                    cnt += 1
                else:
                    break
            ans = max(ans, cnt)

        return ans