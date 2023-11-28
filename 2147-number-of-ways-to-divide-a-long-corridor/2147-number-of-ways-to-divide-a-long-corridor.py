class Solution:
    def numberOfWays(self, corridor: str) -> int:
        ans = 1
        prevSeat = 0
        seat = 0
        mod = (10**9) + 7
        
        for i in range(len(corridor)):
            if corridor[i] == "S" and seat != 2:
                seat += 1
                prevSeat = i
            elif corridor[i] == "S" and seat == 2:
                ans = (ans * (i - prevSeat)) % mod
                seat = 1
        if seat == 1 or seat == 0 and ans == 1:
            return 0
        return ans