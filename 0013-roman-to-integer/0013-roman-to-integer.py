class Solution:
    def romanToInt(self, s: str) -> int:
        cache = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and cache[s[i]] < cache[s[i+1]]:
                res -= cache[s[i]]
            else:
                res += cache[s[i]]
            
        return res