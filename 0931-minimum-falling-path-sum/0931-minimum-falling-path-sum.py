class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        
        for i in range(1, N):
            for j in range(N):
                left = matrix[i-1][j-1] if j-1 >= 0 else float("inf")
                up = matrix[i-1][j]
                right = matrix[i-1][j+1] if j+1 < N else float("inf")
                
                matrix[i][j] += min(left, up, right)
        return min(matrix[-1])
                
        
        
        
#         N = len(matrix)
#         cache = {}
        
#         def path(r, c):
#             if r == N:
#                 return 0
#             if c < 0 or c == N:
#                 return float("inf")
#             if (r, c) in cache:
#                 return cache[(r, c)]
            
#             cache[(r,c)] = matrix[r][c] + min(path(r+1, c-1), path(r+1, c), path(r+1, c+1))
#             return cache[(r, c)]
        
#         res = float("inf")
#         for i in range(len(matrix)):
#             res = min(res, path(0, i))
        
#         return res