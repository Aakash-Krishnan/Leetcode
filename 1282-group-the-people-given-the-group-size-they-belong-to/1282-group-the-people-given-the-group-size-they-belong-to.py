class Solution:
    def groupThePeople(self, A: List[int]) -> List[List[int]]:
        fmap = {}
        ans = []

        for i in range(len(A)):
            if A[i] in fmap:
                fmap[A[i]] += [i]
            else:
                fmap[A[i]] = [i]

        for i in fmap:
            # print(fmap[i]) 
            # print(i)  
            if len(fmap[i]) >= i:
                j = 0
                n = i + j
                while n <= len(fmap[i]):
                    sub = fmap[i][j: n]
                    ans.append(sub)
                    j = n
                    n += i
        return ans