class Solution:
    def rearrangeArray(self, A: List[int]) -> List[int]:
        L, R = 0, 1
        res = [0] * len(A)
        
        for k in range(len(A)):
            if A[k] > 0:
                res[L] = A[k]
                L += 2
            else:
                res[R] = A[k]
                R += 2
        
        return res
                