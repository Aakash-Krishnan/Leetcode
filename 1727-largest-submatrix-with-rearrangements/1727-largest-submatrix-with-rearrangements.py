class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        arr = [[0]*m for _ in range(n)]
        
        for j in range(m):
            for i in range(n-1, -1, -1):
                if matrix[i][j]:
                    arr[i][j] = 1
                    if i < n-1:
                        arr[i][j] += arr[i+1][j]
        ans = 0
        for i in range(n):
            sortArray = sorted(arr[i], reverse=True)
            for j in range(m):
                ans = max(ans, sortArray[j] * (j+1))
        return ans