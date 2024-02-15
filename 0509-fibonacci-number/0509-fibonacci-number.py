class Solution:
    def fib(self, n: int) -> int:
        if  n <= 1:
            return n
        n1 = 0
        n2 = 1
        
        for i in range(2, n+1):
            num = n1 + n2
            n1 = n2
            n2 = num
        
        return n2