class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        q = deque(range(1, 10))
        res = []
        
        while q:
            n = q.popleft()
            if n > high:
                break
            if low <= n <= high:
                res.append(n)
            ones = n % 10
            if ones < 9:
                q.append(n*10 + (ones + 1))
        return res