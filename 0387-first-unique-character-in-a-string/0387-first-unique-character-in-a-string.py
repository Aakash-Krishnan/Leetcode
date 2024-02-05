class Solution:
    def firstUniqChar(self, s: str) -> int:
        smap = Counter(s)
        for i in range(len(s)):
            if smap[s[i]] == 1:
                return i
        return -1