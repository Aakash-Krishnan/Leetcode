class Solution:
    def spiralOrder(self, A: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(A[0])
        top, bottom = 0, len(A)
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(A[top][i])
            top += 1
            for i in range(top, bottom):
                res.append(A[i][right - 1])
            
            right -= 1
            if not (left < right and top < bottom):
                break
            
            for i in range(right - 1, left - 1, -1):
                res.append(A[bottom-1][i])
            bottom -= 1
            
            for i in range(bottom-1, top-1, -1):
                res.append(A[i][left])
            left += 1
        
        return res