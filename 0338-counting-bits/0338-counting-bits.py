class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        
        for i in range(1, n+1):
            pos = 0
            cnt = 0
            while i >> pos:
                cnt += (i>>pos) & 1
                pos += 1
            
            res.append(cnt)
        
        return res