class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":return ""
        
        countT, window = Counter(t), {}
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            if char in countT and window[char] == countT[char]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = (r-l+1)
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l : r+1] if resLen != float("inf") else ""