class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = "".join(s[-1])
        for i in range(len(s)-2, -1 ,-1):
            res += " " + s[i]
        
        return res