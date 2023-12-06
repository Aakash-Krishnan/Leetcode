class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        m = 0
        start = 1

        while m <= n:
            if (m + 7) <= n:
                ans += ((7)*(start + (start + 6))) // 2
            else:
                end = n - m
                ans += ((end)*(start + (start + end-1))) // 2

            start += 1
            m += 7 
        return ans