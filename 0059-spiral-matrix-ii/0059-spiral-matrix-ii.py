class Solution:
    def generateMatrix(self, A: int) -> List[List[int]]:
        arr =[]
        for i in range(A):
            sub = []
            for j in range(A):
                sub.append(0)
            arr.append(sub)

        i, j = 0, 0
        n = 1

        while A > 1:
            for k in range(A-1):
                arr[i][j] = n
                n += 1
                j += 1
            
            for k in range(A-1):
                arr[i][j] = n
                n += 1
                i += 1
            
            for k in range(A-1):
                arr[i][j] = n
                n += 1
                j -= 1
            
            for k in range(A-1):
                arr[i][j] = n
                n += 1
                i -= 1

            i += 1
            j += 1
            A -= 2
        if A == 1:
            arr[i][j] = n
        
        return arr