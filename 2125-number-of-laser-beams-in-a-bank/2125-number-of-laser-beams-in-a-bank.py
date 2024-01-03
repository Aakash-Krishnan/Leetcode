class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        
        for i in range(len(bank)):
            cnt = 0
            for j in range(len(bank[0])):
                if int(bank[i][j]):
                    cnt += 1
            
            if prev:
                ans += (prev * cnt)
            
            if cnt:
                prev = cnt
        return ans