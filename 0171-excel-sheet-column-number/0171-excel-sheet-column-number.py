class Solution:
    def titleToNumber(self, A: str) -> int:
        ans = 0
        po = 0
        for i in range(len(A)-1, -1, -1):
            ans += ((ord(A[i])- 64) * 26**po)
            po += 1
        return ans