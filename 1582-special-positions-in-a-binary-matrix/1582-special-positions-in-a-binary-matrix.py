class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        arr = []
        ans = 0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    arr.append([i, j])
        
        for i in arr:
            L = i[0]
            R = 0
            flag =  False
            while R < len(mat[0]):
                if mat[L][R] and R != i[1]:
                    flag = True
                    break
                R += 1
            
            if not flag:
                L = 0
                R = i[1]
                
                while L < len(mat):
                    if mat[L][R] and L != i[0]:
                        flag = True
                        break
                    L += 1
            
            if not flag:
                ans += 1
        
        return ans