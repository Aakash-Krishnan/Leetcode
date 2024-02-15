class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            sub = [1]
            for j in range(1, i+1):
                if j == i:
                    sub.append(1)
                else:
                    sub.append(res[-1][j] + res[-1][j-1])
            res.append(sub)
        
        return res