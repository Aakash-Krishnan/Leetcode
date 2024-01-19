class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        cache = {}
        
        def path(r, c):
            if r == N:
                return 0
            if c < 0 or c == N:
                return float("inf")
            if (r, c) in cache:
                return cache[(r, c)]
            
            cache[(r,c)] = matrix[r][c] + min(path(r+1, c-1), path(r+1, c), path(r+1, c+1))
            return cache[(r, c)]
        
        res = float("inf")
        for i in range(len(matrix)):
            res = min(res, path(0, i))
        
        return res