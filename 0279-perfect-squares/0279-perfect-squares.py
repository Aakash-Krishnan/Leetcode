class Solution:
    def numSquares(self, n: int) -> int:
        cache = [n] * (n+1)
        cache[0] = 0
        
        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s* s
                if target - square < 0:
                    break
                cache[target] = min(cache[target], 1 + cache[target - square])
        
        return cache[-1]