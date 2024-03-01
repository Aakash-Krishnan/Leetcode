class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        pN, pY = [0] * (n+1), [0] * (n+1)
        
        for i in range(1, n+1):
            pN[i] = pN[i-1]
            if customers[i-1] == 'N':
                pN[i] += 1
        
        for i in range(n-1, -1, -1):
            pY[i] = pY[i+1]
            if customers[i] == 'Y':
                pY[i] += 1
        
        penalty, hour = float("inf"), 0
        for i in range(n+1):
            cnt = pY[i] + pN[i]
            if cnt < penalty:
                penalty = cnt
                hour = i
        
        return hour