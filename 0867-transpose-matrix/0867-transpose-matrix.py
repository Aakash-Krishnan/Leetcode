class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for j in range(len(matrix[0])):
            sub = []
            for i in range(len(matrix)):
                sub.append(matrix[i][j])
            ans.append(sub)
        
        return ans
                