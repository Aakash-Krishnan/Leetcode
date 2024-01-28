class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row, col = len(matrix), len(matrix[0])
        preMat = [[0] * col for _ in range(row)]
        
        for r in range(row):
            for c in range(col):
                top = preMat[r-1][c] if r > 0 else 0
                left = preMat[r][c-1] if c > 0 else 0
                topLeft = preMat[r-1][c-1] if min(r, c) > 0 else 0   
                preMat[r][c] = matrix[r][c] + top + left - topLeft
        
        res = 0
        for r1 in range(row):
            for r2 in range(r1, row):
                cache = defaultdict(int)
                cache[0] = 1
                for c in range(col):
                    currSum = preMat[r2][c] - (
                        preMat[r1-1][c] if r1 > 0 else 0
                    )
                    diff = currSum - target
                    res += cache[diff]
                    cache[currSum] += 1
        
        return res