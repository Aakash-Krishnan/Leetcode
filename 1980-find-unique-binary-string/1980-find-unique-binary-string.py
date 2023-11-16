class Solution:
    def findDifferentBinaryString(self, arr):
        fset = set()
        for i in arr:
            fset.add(i)

        ans = []
        def backTrack(A, idx, flag):
            if idx == len(arr[0]):
                if A not in fset and not flag:
                    ans.append(A[:])
                return

            backTrack(A, idx+1, flag)
            A = A[:idx] + "0" + A[idx+1:]
            backTrack(A, idx+1, flag)
            A = A[:idx] + "1" + A[idx+1:]
            if flag: return 
        
        A = "1" * len(arr[0])
        backTrack(A, 0, False)
        return ans[0]