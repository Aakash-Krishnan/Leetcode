def power(x, n):
    if x == 0:
        return 0
    if n == 0:
        return 1

    half = power(x, n//2)
    if n&1 == 0:
        return half * half
    else:
        return half * half * x

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        result = power(x, abs(n))
        if n >= 0:
            return result
        
        return 1/result