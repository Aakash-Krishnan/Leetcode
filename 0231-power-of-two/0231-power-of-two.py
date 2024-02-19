class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        pos = 0
        while 1<<pos <= n:
            if 1 << pos == n:
                return True
            pos += 1
        
        return False