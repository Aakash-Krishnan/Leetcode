class Solution:
    def candy(self, A: List[int]) -> int:
        candie = [1] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                candie[i] = candie[i-1] + 1
        
        for i in range(len(A)-2, -1, -1):
            if A[i] > A[i+1]:
                candie[i] = max(candie[i], candie[i+1] + 1)
        
        return sum(candie)