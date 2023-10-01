class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        arr = []
        col = len(matrix[0])
        for i in range(len(matrix)):
            for j in range(col):
                if matrix[i][j] == 0:
                    arr.append([i, j])
        
        for i in arr:
            I = i[0]
            J = 0
            while J < col:
                matrix[I][J] = 0
                J += 1
            
            I = 0
            J = i[1]
            while I < len(matrix):
                matrix[I][J] = 0
                I += 1
        
        return matrix