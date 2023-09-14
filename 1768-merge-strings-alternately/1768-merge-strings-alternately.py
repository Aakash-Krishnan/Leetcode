class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = ''
        i = 0
        while i < len(word1) and i < len(word2):
            l += word1[i]
            l += word2[i]
            
            i += 1
        
        if i < len(word1):
            l += word1[i:]
        elif i < len(word2):
            l += word2[i:]
        return l