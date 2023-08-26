class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # arr = []
        ans = 0
        for i in range(n):
            N = start + 2 * i
            ans ^= N
        return ans
        