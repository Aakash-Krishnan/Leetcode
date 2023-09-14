class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        L = 0
        length = 0
        
        for r in range(len(s)):
            char = s[r]
            
            if char in seen and seen[char] >= L:
                L = seen[char] + 1
            else:
                length = max(length, (r - L + 1))
            seen[char] = r
        return length
