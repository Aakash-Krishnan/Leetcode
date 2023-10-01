class Solution:
    def reverseWords(self, s: str) -> str:
        I = -1
        ans = ""
        for i in range(len(s)):
            if s[i] == " ":
                for j in range(i-1, I, -1):
                    ans += s[j]
                if len(s)-1 != i:
                    ans += " "
                I = i
        for j in range(len(s)-1, I, -1):
            ans += s[j]

        return ans