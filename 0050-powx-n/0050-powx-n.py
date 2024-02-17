class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(a, b):
            if not b:return 1
            if not a:return 0

            
            half = power(a, b//2)
            if b&1:
                return half * half * a
            return half * half
        
        value = power(x, abs(n))
        if n >= 0:
            return value
        return 1/value