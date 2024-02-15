class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(1, len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(len(matrix)):
            L, R = 0, len(matrix[0])-1
            while L < R:
                matrix[i][L], matrix[i][R] = matrix[i][R], matrix[i][L]
                L += 1
                R -= 1
        
        return matrix