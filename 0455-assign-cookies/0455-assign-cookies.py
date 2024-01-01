class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        ans = 0
        i, j = 0, 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ans += 1
                i += 1
                j += 1
            else:
                j += 1
        return ans