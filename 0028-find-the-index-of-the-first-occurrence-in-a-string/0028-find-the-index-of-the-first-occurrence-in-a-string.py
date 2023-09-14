class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 1:
            if needle == haystack:
                return 0
        L = 0
        R = len(needle)
        while R <= len(haystack):
            if haystack[L: R] == needle:
                return L
            L += 1
            R += 1
        return -1