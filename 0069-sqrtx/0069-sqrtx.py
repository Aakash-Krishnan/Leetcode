class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x
        ans = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            sqt = mid * mid
            if sqt <= x:
                ans = mid
                lo = mid + 1
            elif sqt > x:
                hi = mid - 1

        return ans