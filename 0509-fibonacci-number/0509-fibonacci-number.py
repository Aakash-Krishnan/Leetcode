class Solution:
    def fib(self, n: int, cache={}) -> int:
        if n in cache: return cache[n]
        if not  n: return 0
        if n <= 2:
            return 1
        
        cache[n] = self.fib(n-1) + self.fib(n-2)
        return cache[n]