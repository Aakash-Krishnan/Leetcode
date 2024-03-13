class Solution:
    def pivotInteger(self, n: int) -> int:
        l, r = 1, n
        lSum, rSum = l, r
        
        while l <= r:
            if l == r and lSum == rSum:
                return l
            elif lSum < rSum:
                l += 1
                lSum += l
            else:
                r -= 1
                rSum += r
        return -1